
import FWCore.ParameterSet.Config as cms


# file organized like this:
# COLLECTIONS
# CUTS
# DEBUG
# SELECTORS
# BOOLS
# OTHER

from HiggsAnalysis.HiggsTo2photons.hggPhotonIDCuts_cfi import *
#from CMGTools.External.pujetidsequence_cff   import puJetMva
from CMGTools.External.pujetidproducer_cfi import stdalgos, chsalgos
#from HiggsAnalysis.HiggsToGammaGamma.PhotonFixParams4_2_cfi import *
from PhysicsTools.SelectorUtils.pfJetIDSelector_cfi import pfJetIDSelector

h2ganalyzer = cms.EDAnalyzer(
    "GlobeAnalyzer",
    RootFileName = cms.string('prova.root'),
    JobMaker = cms.string('jobmaker unknown'),

    # RUNNING MODULES
    doGenerator = cms.bool(False),
    doReducedGen = cms.bool(False),
    doGenParticles = cms.bool(True),
    doGenVertices = cms.bool(False),
    
    doGenJet_algo1 = cms.bool(True),
    doGenJet_algo2 = cms.bool(False),
    doGenJet_algo3 = cms.bool(False),

    doGenMet = cms.bool(False),
    
    doSimHits = cms.bool(False),
    doSimTracks = cms.bool(False),
    doSimTrackPlusSimVertex = cms.bool(False),
    
    doTrackingParticles = cms.bool(False),
    
    doTkRecHits = cms.bool(False),
    doEcalRecHits = cms.bool(False),
    
    doPreshowerHits = cms.bool(False),
    doEcal = cms.bool(False),
    doHcal = cms.bool(False),
    doHFHcal = cms.bool(False),
    
    doCaloTower = cms.bool(False),
    
    doL1 = cms.bool(False),
    doHLT = cms.bool(False),
    
    doTracks = cms.bool(False),
    doGsfTracks = cms.bool(False),

    doVertices_std = cms.bool(False),
    doVertices_nobs = cms.bool(False),
    
    doElectron_std = cms.bool(False),
    doMuon = cms.bool(False),
    doPhoton = cms.bool(False),
    doAllConversions = cms.bool(False),
    doLeptons = cms.bool(False),
    
    doJet_algo1 = cms.bool(False),
    doJet_algo2 = cms.bool(False),
    doJet_algo3 = cms.bool(False),
    doJet_algoPF1 = cms.bool(False),
    doJet_algoPF2 = cms.bool(False),
    doJet_algoPF3 = cms.bool(False),

    doPFCandidates = cms.bool(False),
    PFIsoOuterCone = cms.double(0.4),
    
    doMet = cms.bool(False),
    dotcMet = cms.bool(False),
    doPFMet = cms.bool(False),
    doHt = cms.bool(False),
    
    doRho = cms.bool(False),
    doPileup = cms.bool(False),
    doPdfWeight = cms.bool(False),
    PdfWeightsCollList = cms.VInputTag(cms.InputTag("pdfWeights","cteq66")),

    doFastSim = cms.bool(False),
    doAodSim  = cms.bool(False),
    doParticleGun = cms.bool(False),
    
    storeGsfTracksOnlyIfElectrons = cms.bool(False),


    energyCorrectionsFromDB = cms.bool(False),
    energyCorrectionsFileNamePho = cms.string("gbrv3ph_52x.root"),
    energyCorrectionsFileNameEle = cms.string("gbrv3ele_52x.root"),
    energyCorrectionsVersion = cms.string("V3"),
    globalCounters = cms.vstring(),

    #PhotonFIX parameters
    #PFParameters = PhotonFixParameters,

    # COLLECTIONS
    GeneratorColl = cms.InputTag("generator"),
    GenParticlesColl = cms.InputTag("genParticles"),
    GlobeReducedGendRMin = cms.double(0.3),
    
    pileupInfoCollection = cms.InputTag("addPileupInfo"),
    
    GenJetColl_algo1 = cms.InputTag("ak5GenJets"),
    GenJetColl_algo2 = cms.InputTag("ak7GenJets"),
    GenJetColl_algo3 = cms.InputTag("kt4GenJets"),

    GenCaloMETColl = cms.InputTag("genMetCalo"),
    GenTrueMETColl = cms.InputTag("genMetTrue"),
    GenNoptMETColl = cms.InputTag("genMetCaloAndNonPrompt"),
    
    SimHitList = cms.VInputTag(cms.InputTag("g4SimHits","TrackerHitsPixelBarrelLowTof"),
                               cms.InputTag("g4SimHits","TrackerHitsPixelBarrelHighTof"),
                               cms.InputTag("g4SimHits","TrackerHitsPixelEndcapLowTof"),
                               cms.InputTag("g4SimHits","TrackerHitsPixelEndcapHighTof"),
                               cms.InputTag("g4SimHits","TrackerHitsTIBLowTof"), 
                               cms.InputTag("g4SimHits","TrackerHitsTIBHighTof"),
                               cms.InputTag("g4SimHits","TrackerHitsTIDLowTof"),
                               cms.InputTag("g4SimHits","TrackerHitsTIDHighTof"),
                               cms.InputTag("g4SimHits","TrackerHitsTOBLowTof"),
                               cms.InputTag("g4SimHits","TrackerHitsTOBHighTof"), 
                               cms.InputTag("g4SimHits","TrackerHitsTECLowTof"),
                               cms.InputTag("g4SimHits","TrackerHitsTECHighTof")),
    SimHitPixBarrelLowColl = cms.InputTag("g4SimHits","TrackerHitsPixelBarrelLowTof"),
    SimHitPixEndcapLowColl = cms.InputTag("g4SimHits","TrackerHitsPixelEndcapLowTof"),
    SimHitTIBLowColl = cms.InputTag("g4SimHits","TrackerHitsTIBLowTof"),
    SimHitTOBLowColl = cms.InputTag("g4SimHits","TrackerHitsTOBLowTof"),
    SimHitTIDLowColl = cms.InputTag("g4SimHits","TrackerHitsTIDLowTof"),
    SimHitTECLowColl = cms.InputTag("g4SimHits","TrackerHitsTECLowTof"),
    
    SimTrackColl = cms.InputTag("g4SimHits"),
    SimTrackPlusSimVertex = cms.bool(False),                   
    SimVertexColl = cms.InputTag("g4SimHits"),
    
    TPColl = cms.InputTag("mergedtruth","MergedTrackTruth"),
    TVColl = cms.InputTag("mergedtruth","MergedTrackTruth"),
    
    PixelRecHitsColl = cms.InputTag("siPixelRecHits"),
    RphiRecHitsColl = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),                       
    MatchedRecHitsColl = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
    StereoRecHitsColl = cms.InputTag("siStripMatchedRecHits","stereoRecHit"),
    
    EcalHitEBColl = cms.InputTag("reducedEcalRecHitsEB"),
    EcalHitEEColl = cms.InputTag("reducedEcalRecHitsEE"),
    EcalHitESColl = cms.InputTag("reducedEcalRecHitsES"),
        
    HcalHitsBEColl = cms.InputTag("reducedHcalRecHits", "hbhereco"),
    HcalHitsFColl = cms.InputTag("reducedHcalReHits", "hfreco"), 
    HcalHitsHoColl = cms.InputTag("reducedHcalRecHits", "horeco"),
    
    CaloTowerColl = cms.InputTag("towerMaker"),
    
    BarrelBasicClusterColl = cms.InputTag("",""),
    EndcapBasicClusterColl = cms.InputTag("multi5x5SuperClusters","multi5x5EndcapBasicClusters"),    
    #EndcapBasicClusterColl = cms.InputTag("multi5x5BasicClusters","multi5x5EndcapBasicClusters"),    
    BarrelBasicClusterShapeColl = cms.InputTag("",""),
    BarrelHybridClusterShapeColl = cms.InputTag("hybridSuperClusters","hybridShapeAssoc"),
    EndcapBasicClusterShapeColl = cms.InputTag("multi5x5SuperClusters","multi5x5EndcapShapeAssoc"),
    BarrelSuperClusterColl = cms.InputTag("multi5x5SuperClusters","multi5x5BarrelSuperClusters"),
    BarrelHybridClusterColl = cms.InputTag("hybridSuperClusters","hybridBarrelBasicClusters"),
    EndcapSuperClusterColl = cms.InputTag("correctedMulti5x5SuperClustersWithPreshower"),
    HybridSuperClusterColl = cms.InputTag("correctedHybridSuperClusters"),
    
    TrackColl = cms.InputTag("generalTracks"),
    GsfTrackColl = cms.InputTag("electronGsfTracks"),

    # Temporary
    TrackColl2 = cms.InputTag("generalTracks"),
    TrackColl3 = cms.InputTag("electronGsfTracks"),
    AssocLabel = cms.string('TrackAssociatorByHits'),
    
    ElectronColl_std = cms.InputTag("gsfElectrons"),        
    eIDLabels        = cms.VInputTag(cms.InputTag("eidLoose"),
                                     cms.InputTag("eidTight")),
    electronMVAWeightFileName =  cms.FileInPath("RecoEgamma/ElectronIdentification/data/TMVA_BDTSimpleCat_17Feb2011.weights.xml"),
    IsoValElectronPF = cms.VInputTag(cms.InputTag('elPFIsoValueCharged03PFIdPFIso'),
                                     cms.InputTag('elPFIsoValueGamma03PFIdPFIso'),
                                     cms.InputTag('elPFIsoValueNeutral03PFIdPFIso')),
 
                                
    PhotonCollStd = cms.InputTag("photons"),
    PhotonCollPf = cms.InputTag("pfPhotonTranslator:pfphot"),
    ConvertedPhotonColl = cms.InputTag("allConversions"),
    MuonColl = cms.InputTag("muons"),
    RhoCollectionForMuons = cms.InputTag("kt6PFJetsCentralNeutral","rho"),
    
    JetCorrectionMC_algoPF1   = cms.untracked.string("ak5PFL1FastL2L3"),
    JetCorrectionData_algoPF1 = cms.untracked.string("ak5PFL1FastL2L3Residual"),

    JetCorrectionMC_algoPF2   = cms.untracked.string("ak7PFL1FastL2L3"),
    JetCorrectionData_algoPF2 = cms.untracked.string("ak7PFL1FastL2L3Residual"),

    JetCorrectionMC_algoPF3   = cms.untracked.string("ak5PFchsL1FastL2L3"),
    JetCorrectionData_algoPF3 = cms.untracked.string("ak5PFchsL1FastL2L3Residual"),


    #std::vector<JetCorrectorParameters> params;
    JetColl_algo1 = cms.InputTag("ak5CaloJets"),
    JetColl_algo2 = cms.InputTag("ak7CaloJets"),
    JetColl_algo3 = cms.InputTag("kt4CaloJets"),
    JetColl_algoPF1 = cms.InputTag("ak5PFJets"),
    JetColl_algoPF2 = cms.InputTag("ak7PFJets"),
    JetColl_algoPF3 = cms.InputTag("ak5PFchsJets"),
    
    puJetIDAlgos_algoPF1 = cms.untracked.VPSet(stdalgos),
    puJetIDAlgos_algoPF2 = cms.untracked.VPSet(stdalgos),
    puJetIDAlgos_algoPF3 = cms.untracked.VPSet(chsalgos),

    pfLooseId = pfJetIDSelector.clone(),
    
    #bcBColl = cms.InputTag("hybridSuperClusters","hybridBarrelBasicClusters"),
    #bcEColl = cms.InputTag("multi5x5BasicClusters","multi5x5EndcapBasicClusters"),
    tkColl = cms.InputTag("generalTracks"),                                                 

    JetTrackAssociationColl_algoPF1 = cms.InputTag("ak5JetTracksAssociatorAtVertex"),    
    JetTrackAssociationColl_algoPF2 = cms.InputTag("ak7JetTracksAssociatorAtVertex"),
    JetTrackAssociationColl_algoPF3 = cms.InputTag(""),
    
    rhoCollection_algo1 = cms.InputTag("kt6PFJets","rho"),
    rhoCollection_algo2 = cms.InputTag("kt6CaloJets","rho"),
    rhoCollection_algo3 = cms.InputTag("kt6CaloJetsCentral","rho"),

    PFCandidateColl = cms.InputTag("particleFlow"),
    isolationValues03 = cms.PSet(pfChargedHadrons = cms.InputTag('isoValPhotonWithCharged03'),
                                 pfPhotons        = cms.InputTag('isoValPhotonWithPhotons03'),
                                 pfNeutralHadrons = cms.InputTag('isoValPhotonWithNeutral03'),
                                 ),

    isolationValues04 = cms.PSet(pfChargedHadrons = cms.InputTag('isoValPhotonWithCharged04'),
                                 pfPhotons        = cms.InputTag('isoValPhotonWithPhotons04'),
                                 pfNeutralHadrons = cms.InputTag('isoValPhotonWithNeutral04'),
                                 ),
    
    CaloMETColl = cms.InputTag("met"),
    TcMETColl = cms.InputTag("tcMet"),
    PFMETColl = cms.InputTag("pfMet"),

    BeamSpot = cms.InputTag("offlineBeamSpot"),
    VertexColl_std = cms.InputTag("offlinePrimaryVerticesWithBS"),
    VertexColl_nobs = cms.InputTag("offlinePrimaryVertices"),
    
    L1EtMiss = cms.InputTag("l1extraParticles","MET"),    
    L1CenJet = cms.InputTag("l1extraParticles","Central"),
    L1ForJet = cms.InputTag("l1extraParticles","Forward"),    
    L1TauJet = cms.InputTag("l1extraParticles","Tau"),
    L1EMNonIso = cms.InputTag("l1extraParticles","NonIsolated"),
    L1EMIso = cms.InputTag("l1extraParticles","Isolated"),
    L1Mu = cms.InputTag("l1extraParticles"),
    L1GtReadoutRecordTag = cms.InputTag("gtDigis"),
    #L1GtObjectMapRecordTag = cms.InputTag("hltL1GtObjectMap"),
    L1GtObjectMapRecordTag = cms.InputTag("L1GlobalTriggerReadoutRecord"),
    HLTParameters = cms.PSet(
    useSecondaryTrigger = cms.bool(False),
    PrimaryTriggerResultsTag   = cms.InputTag("TriggerResults"      ,"","HLT"),
    TriggerResultsTag          = cms.InputTag("hltTriggerSummaryAOD","","HLT")
    ),
    # Use this in case 2 different HLTs are stored, like 8e29 and 1e31
    # useSecondaryTrigger = cms.bool(True),
    # PrimaryTriggerResultsTag   = cms.InputTag("TriggerResults"      ,"","HLT8E29"),
    # SecondaryTriggerResultsTag = cms.InputTag("TriggerResults"      ,"","HLT"    ),
    # TriggerResultsTag          = cms.InputTag("hltTriggerSummaryAOD","","HLT8E29")),
    
    # CUTS
    hggPhotonIDConfiguration = cms.PSet(hggPhotonIDCuts),
    
    GeneratorCuts = cms.PSet(EtCut = cms.double(5.0)),
    GenJetCuts = cms.PSet(EtCut = cms.double(-1.0)),
    
    SimHitCuts = cms.PSet(EnergyCut = cms.double(0.0)),
    SimTrackCuts = cms.PSet(EnergyCut = cms.double(0.0)),
    
    EcalHitCuts = cms.PSet(BarrelEnergyCut = cms.double(0.0),
                           EndcapEnergyCut = cms.double(0.0),
                           PreEnergyCut = cms.double(-999.0),
                           EcalMaxDR = cms.double(0.5),
                           KeepOutsideCone = cms.bool(False)),
    
    HcalHitsCuts = cms.PSet(HBHEEnergyCut = cms.double(0.35),
                            HFEnergyCut = cms.double(1.0),
                            HOEnergyCut = cms.double(0.7),
                            HcalMaxDR = cms.double(0.6),
                            KeepOutsideCone = cms.bool(False)),
    
    BasicClusterCuts = cms.PSet(EnergyCut = cms.double(-1.0)),
    SuperClusterCuts = cms.PSet(EnergyCut = cms.double(-1.0)),
    CaloTowerCuts = cms.PSet(EtCut = cms.double(1.0)),
    
    TrackCuts = cms.PSet(PtCut = cms.double(-1.0)),
    
    TPCuts = cms.PSet(tpLvpCut = cms.double(99999.0),
                      tpEtaCut = cms.double(2.5),
                      tpTvpCut = cms.double(99999.0),
                      tpPtCut = cms.double(1.0),
                      tpPdgidCut = cms.vint32(11, 22)),
    IsoCuts = cms.PSet(InnerCone = cms.double(0.015),
                       OuterCone = cms.double(0.3)),
    
    ElectronCuts = cms.PSet(EtCut = cms.double(0.0)),
    MuonCuts = cms.PSet(PtCut = cms.double(-1.0)),
    PhotonCuts = cms.PSet(EtCut = cms.double(0.0)),
    ConvertedPhotonCuts = cms.PSet(EtCut = cms.double(0.0)),
    JetCuts = cms.PSet(EnergyCut = cms.double(5.0)),

    GenParticleCuts = cms.PSet(EtCut = cms.double(0.0),
                               PdgId = cms.vint32(),
                               Keep = cms.bool(True)),

    # DEBUG
    Debug_Level = cms.int32(0),
    
    # SELECTORS
    SelectorNumber = cms.int32(0),
    SelectorCuts0 = cms.PSet(RecoPhotonNumber = cms.int32(1000),
                             RecoMuonNumber = cms.int32(1000),
                             RecoElectronNumber = cms.int32(1000),
                             MCLepPhotNumber = cms.int32(1000),
                             MCetcutel= cms.double(10.),
                             MCetcutmu= cms.double(10.),
                             MCetcutph= cms.double(10.),
                             MCetacutel= cms.double(2.7),
                             MCetacutmu= cms.double(2.7),
                             MCetacutph= cms.double(2.7),
                             nMCel = cms.int32(2000),
                             nMCmu = cms.int32(2000),
                             nMCph = cms.int32(2000),
                             nMCelmu = cms.int32(2),
                             nMCelph = cms.int32(2000),
                             nMCmuph = cms.int32(2000),
                             nMCelmuph = cms.int32(2000),
                             Recoetcutel= cms.double(10.),
                             Recoetcutmu= cms.double(10.),
                             Recoetcutph= cms.double(10.),
                             Recoetacutel= cms.double(2.7),
                             Recoetacutmu= cms.double(2.7),
                             Recoetacutph= cms.double(2.7),
                             nRecoel = cms.int32(2000),
                             nRecomu = cms.int32(2000),
                             nRecoph = cms.int32(2000),
                             nRecoelmu = cms.int32(2),
                             nRecoelph = cms.int32(2000),
                             nRecomuph = cms.int32(2000),
                             nRecoelmuph = cms.int32(2000)),
    

    #PAT
    
    electronTag = cms.untracked.InputTag("cleanPatElectrons"),
    photonTag   = cms.untracked.InputTag("cleanPatPhotons"),
    muonTag     = cms.untracked.InputTag("cleanPatMuons"),
    jetTag   = cms.untracked.InputTag("cleanPatJets"),
    
    # MISCELLANEOUS
    TrackAssociatorParameters = cms.PSet(muonMaxDistanceSigmaX = cms.double(0.0),
                                         muonMaxDistanceSigmaY = cms.double(0.0),
                                         CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
                                         dRHcal = cms.double(1.0),
                                         # bool   accountForTrajectoryChangeMuon = true
                                         # matching requirements 
                                         dREcal = cms.double(1.0),
                                         CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
                                         # association types
                                         useEcal = cms.bool(True),
                                         # preselection requirements in theta-phi space
                                         # allowed range: 
                                         #   dTheta = +/- dR
                                         #   dPhi = +/- dR  
                                         # (track trajectory changes are taken into account for muons)
                                         dREcalPreselection = cms.double(1.0),
                                         HORecHitCollectionLabel = cms.InputTag("horeco"),
                                         dRMuon = cms.double(9999.0),
                                         crossedEnergyType = cms.string('SinglePointAlongTrajectory'),
                                         propagateAllDirections = cms.bool(True),
                                         muonMaxDistanceX = cms.double(5.0),
                                         muonMaxDistanceY = cms.double(5.0),
                                         useHO = cms.bool(True), ## RecoHits
                                         
                                         accountForTrajectoryChangeCalo = cms.bool(False),
                                         DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
                                         EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
                                         dRHcalPreselection = cms.double(1.0),
                                         useMuon = cms.bool(False), ## RecoHits
                                         
                                         useCalo = cms.bool(False), ## CaloTowers
                                         
                                         # input tags
                                         EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
                                         dRMuonPreselection = cms.double(0.2),

    usePreshower = cms.bool(False),
    dRPreshowerPreselection = cms.double(0.2),
    trajectoryUncertaintyTolerance = cms.double(-1.0),
                                         
                                         truthMatch = cms.bool(False), ## debugging information
                                         
                                         HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
                                         useHcal = cms.bool(True) ## RecoHits
                                         )
    )

