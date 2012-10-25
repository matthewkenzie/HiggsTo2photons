#!/usr/bin/env python
import os
import time
import threading
import shutil
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-d", "--datacard", dest="datacard", help="Input Datacard")
parser.add_option("-e", "--Expected", action="store_true", dest="Expected", default=True, help="Do Expected PValues")
parser.add_option("-o", "--Observed", action="store_true", dest="Observed", default=False, help="Do Observed PValues")
parser.add_option("-c", "--Categories", action="store_true", dest="Categories", default=False, help="Do PValues for all categories")
parser.add_option("-u", "--CustumCat", dest="CustumCat", default="", help="Make datacards and do PValues for custum category --CustumCat=\"cat0 cat1 cat2 cat3\" ")
parser.add_option("-s", "--OutputDirectory", dest="OutputDirectory", default="", help="Output Directory")
parser.add_option("-t", "--toysFile", dest="toysFile", default="", help="Asimov Toy Set File")

parser.add_option("--debug", action="store_true", dest="debug", default=False, help="Enable Debug Mode")
parser.add_option("--dryrun", action="store_true", dest="dryrun", default=False, help="Don't calculate pvalues, but it will still make datacards.")
parser.add_option("--expectSignal", dest="expectSignal", default=1, help="Expected Signal Strength")
parser.add_option("--threads", type="int", dest="threads", default=0, help="Maximum Number of Threads")
parser.add_option("--overwrite", action="store_true", dest="overwrite", default=False, help="Overwrite output directory")
parser.add_option("--RegularMasses", action="store_true", dest="RegularMasses", default=False, help="Only run pvalues at 110-150 in 5 GeV steps.")
parser.add_option("--NoPValue", action="store_true", dest="NoPValue", default=False, help="Don't Calculate pvalues for the given datacard.")
(options, args) = parser.parse_args()

if options.datacard=="":
    print "Must provide datacard!"
    exit(1)

if options.threads==0:
    options.threads=int(os.popen("cat /proc/cpuinfo | grep processor | awk '{print $3}' | tail -1 | xargs -i echo '{}+1' | bc").readlines()[0].strip('\n'))
if options.debug: print "Max Threads:",options.threads

Masses=[x * 0.1 for x in range(1100,1501,10)]
if options.RegularMasses:
    Masses=range(110,151,5)

if options.debug and options.RegularMasses: print "Running with restricted masses:",Masses
else: print "Running with full mass range:",Masses

if options.toysFile!="": options.toysFile=os.path.abspath(options.toysFile)

#Make Datacards
DatacardList=[]
if not options.NoPValue:
    DatacardList.append(os.path.abspath(options.datacard))

basedir=os.getcwd()

if options.Categories:
    categories=os.popen("grep bin "+options.datacard+" | grep cat | grep -v combine | head -n 1 | sed 's|bin[ \\t][ \\t]*||'").readlines()[0].strip("\n")
    categorylist=categories.split(" ")
    if options.debug: print "Category List:",categorylist
    for cat in categorylist:
        veto=""
        for catveto in categorylist:
            if cat==catveto: continue
            veto+="|ch1_"+catveto
        veto=veto[1:]
        if options.debug: print "Veto string for",cat,":",veto
        outputdatacardname=basedir+"/"+os.path.basename(options.datacard).replace(".txt","_"+cat+".txt")
        if options.debug: print "combineCards.py --xc=\""+veto+"\" "+os.path.abspath(options.datacard)+" >& "+outputdatacardname
        os.system("combineCards.py --xc=\""+veto+"\" "+os.path.abspath(options.datacard)+" >& "+outputdatacardname)
        DatacardList.append(outputdatacardname)


if options.CustumCat!="":
    categorylist=os.popen("grep bin "+options.datacard+" | grep cat | grep -v combine | head -n 1 | sed 's|bin[ \\t][ \\t]*||'").readlines()[0].strip("\n").split(" ")
    keeplist=options.CustumCat.split(" ")
    veto=""
    for cat in categorylist:
        vetocat=True
        for keepcat in keeplist:
            if keepcat==cat: vetocat=False
        if vetocat: veto+="|ch1_"+cat
    veto=veto[1:]
    cat=options.CustumCat.replace(" ","")
    if options.debug: print "Veto string for",cat,":",veto
    outputdatacardname=basedir+"/"+os.path.basename(options.datacard).replace(".txt","_"+cat+".txt")
    if options.debug: print "combineCards.py --xc=\""+veto+"\" "+os.path.abspath(options.datacard)+" >& "+outputdatacardname
    os.system("combineCards.py --xc=\""+veto+"\" "+os.path.abspath(options.datacard)+" >& "+outputdatacardname)
    DatacardList.append(outputdatacardname)

for datacard in DatacardList:

    print "Running on datacard:",os.path.basename(datacard)
    datacardoutputdir=os.path.basename(datacard)[:os.path.basename(datacard).rfind(".txt")]
    if options.OutputDirectory!="": datacardoutputdir=options.OutputDirectory+"/"+datacardoutputdir
    if options.toysFile=="": datacardoutputdirexpected=datacardoutputdir+"_Expected_"+str(options.expectSignal)+"SM"
    if options.toysFile!="": datacardoutputdirexpected=datacardoutputdir+"_Expected_"+str(options.expectSignal)+"SM_Asimov"

    if options.OutputDirectory!="":
        if os.path.exists(options.OutputDirectory) and options.overwrite: shutil.rmtree(options.OutputDirectory)
        os.makedirs(options.OutputDirectory)
    if options.Observed:
        if os.path.exists(datacardoutputdir) and options.overwrite: shutil.rmtree(datacardoutputdir)
        os.makedirs(datacardoutputdir)
        datacardoutputdir=os.path.abspath(datacardoutputdir)
    if options.Expected:
        if os.path.exists(datacardoutputdirexpected) and options.overwrite: shutil.rmtree(datacardoutputdirexpected)
        os.makedirs(datacardoutputdirexpected)
        datacardoutputdirexpected=os.path.abspath(datacardoutputdirexpected)

    threadlist=[]
    threads=0
    for mass in Masses:
        time.sleep(0.1)
        threads=int(os.popen("ps | grep combine | wc -l").readline())
        if options.debug: print threads,"threads running. Maximum Threads:",options.threads
        while threads>=options.threads:
            time.sleep(0.25)
            threads=int(os.popen("ps | grep combine | wc -l").readline())
        if options.Observed:
            os.chdir(datacardoutputdir)
            if options.debug: print "combine "+datacard+" -m "+str(mass)+" -M ProfileLikelihood -t 0 -s -1 -n PValue --signif --pvalue >& higgsCombinePValue.ProfileLikelihood.mH"+str(mass)+".log &"
            if not options.dryrun: os.system("combine "+datacard+" -m "+str(mass)+" -M ProfileLikelihood -t 0 -s -1 -n PValue --signif --pvalue >& higgsCombinePValue.ProfileLikelihood.mH"+str(mass)+".log &")
        if options.Expected and options.toysFile=="":
            os.chdir(datacardoutputdirexpected)
            if options.debug: print "combine "+datacard+" -m "+str(mass)+" -M ProfileLikelihood -t -1 -s -1 -n PValueExpected --signif --pvalue --expectSignal="+str(options.expectSignal)+" >& higgsCombinePValueExpected.ProfileLikelihood.mH"+str(mass)+".log &"
            if not options.dryrun: os.system("combine "+datacard+" -m "+str(mass)+" -M ProfileLikelihood -t -1 -s -1 -n PValueExpected --signif --pvalue --expectSignal="+str(options.expectSignal)+" >& higgsCombinePValueExpected.ProfileLikelihood.mH"+str(mass)+".log &")
        if options.Expected and options.toysFile!="":
            os.chdir(datacardoutputdirexpected)
            if options.debug: print "combine "+datacard+" -m "+str(mass)+" -M ProfileLikelihood -t -1 -s -1 -n PValueExpected --signif --pvalue --expectSignal="+str(options.expectSignal)+" --toysFile="+options.toysFile+" >& higgsCombinePValueExpected.ProfileLikelihood.mH"+str(mass)+".log &"
            if not options.dryrun: os.system("combine "+datacard+" -m "+str(mass)+" -M ProfileLikelihood -t -1 -s -1 -n PValueExpected --signif --pvalue --expectSignal="+str(options.expectSignal)+" --toysFile="+options.toysFile+" >& higgsCombinePValueExpected.ProfileLikelihood.mH"+str(mass)+".log &")

    os.chdir(basedir)
    threads=int(os.popen("ps | grep combine | wc -l").readline())
    while threads>=1:
        time.sleep(2)
        threads=int(os.popen("ps | grep combine | wc -l").readline())
    if options.debug: print threads,"threads running",options.threads
    if options.Observed and not options.dryrun: os.system("hadd -f higgsCombinePValue."+os.path.basename(datacardoutputdir)+".ProfileLikelihood.root "+datacardoutputdir+"/higgsCombinePValue.ProfileLikelihood.mH[0-9][0-9]*.[0-9-][0-9]*.root >& "+datacardoutputdir+"/higgsCombinePValue.ProfileLikelihood.log &")
    if options.Expected and not options.dryrun: os.system("hadd -f higgsCombinePValue."+os.path.basename(datacardoutputdirexpected)+".ProfileLikelihood.root "+datacardoutputdirexpected+"/higgsCombinePValueExpected.ProfileLikelihood.mH[0-9][0-9]*.[0-9-][0-9]*.root >& "+datacardoutputdirexpected+"/higgsCombinePValueExpected.ProfileLikelihood.log &")
    
print "Done!"
