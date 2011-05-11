#ifndef GLOBEECALCLUSTERS_H
#define GLOBEECALCLUSTERS_H

#include "FWCore/Framework/interface/Event.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "HiggsAnalysis/HiggsTo2photons/interface/Limits.h"
#include "HiggsAnalysis/HiggsTo2photons/interface/GlobeCuts.h"

#include "TTree.h"
#include "TClonesArray.h"
#include "TLorentzVector.h"

#include "DataFormats/EgammaCandidates/interface/GsfElectron.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectronFwd.h"

#include "DataFormats/EgammaCandidates/interface/Photon.h"
#include "DataFormats/EgammaCandidates/interface/PhotonFwd.h"
#include "DataFormats/EgammaReco/interface/SuperCluster.h"
#include "DataFormats/EgammaReco/interface/SuperClusterFwd.h"
#include "DataFormats/EgammaReco/interface/BasicCluster.h"
#include "DataFormats/EgammaReco/interface/BasicClusterFwd.h"
#include "DataFormats/EgammaReco/interface/BasicClusterShapeAssociation.h"
#include "DataFormats/EgammaReco/interface/ClusterShapeFwd.h"
#include "DataFormats/EcalDetId/interface/EcalSubdetector.h"

#include "Geometry/CaloTopology/interface/CaloTopology.h"
#include "Geometry/CaloGeometry/interface/CaloGeometry.h"

#include "Math/VectorUtil.h"
#include <iostream>

class CaloSubdetectorTopology;

class GlobeEcalClusters {
 public:
  
  GlobeEcalClusters(const edm::ParameterSet&, const char* n="unused");
  virtual ~GlobeEcalClusters() {};

  void defineBranch(TTree* tree);
  bool analyze(const edm::Event&, const edm::EventSetup&);

protected:
  void analyzeBarrelSuperClusters();

  void analyzeEndcapSuperClusters();

  void analyzeEndcapBasicClusters();

  void analyzeBarrelHybridClusters();

public:

  void e2xNOe5xN(float&, float&, const reco::SuperCluster*, const EcalRecHitCollection*, const CaloSubdetectorTopology*);

  //----------------------------------------
protected:
  /** handles to superclusters */
  edm::Handle<reco::SuperClusterCollection> superClustersHybridH; 
  edm::Handle<reco::SuperClusterCollection> superClustersEndcapH; 

  /** handles to basic clusters */
  edm::Handle<reco::BasicClusterCollection> hybridClustersBarrelH; 
  edm::Handle<reco::BasicClusterCollection> basicClustersEndcapH; 
  edm::Handle<reco::BasicClusterCollection> basicClustersBarrelH;


  /** rechits of the current event (initialized in analyze(..)) */
  const EcalRecHitCollection *barrelRecHits;
  const EcalRecHitCollection *endcapRecHits;

  /** calorimeter topology (for the current event) */
  const CaloTopology *topology;

  const CaloGeometry *geometry;

public:
  //----------------------------------------
  // variables for the output ROOT tree 
  //----------------------------------------

// SUPER CLUSTERS
  TClonesArray *sc_p4;
  TClonesArray *sc_islbar_p4;
  TClonesArray *sc_xyz;
  TClonesArray *sc_islbar_xyz;
  TClonesArray *bc_p4;
  TClonesArray *bc_xyz;

  //Island in barrel
  Int_t sc_islbar_n;
  Float_t sc_islbar_raw[MAX_SUPERCLUSTERS];

//CHECK, bad name, it is the energy??? DO WE NEED THIS? WE HAVE THE INDEX TO THE SEED CLUSTER
  Float_t sc_islbar_seedenergy[MAX_SUPERCLUSTERS];

  Int_t sc_islbar_nbc[MAX_SUPERCLUSTERS];

  Int_t sc_islbar_bcseedind[MAX_SUPERCLUSTERS];
  Int_t sc_islbar_bcind[MAX_SUPERCLUSTERS][MAX_SUPERCLUSTER_BASICCLUSTERS];

  Int_t sc_n;
  Int_t sc_hybrid_n;
  Int_t sc_islend_n;
  Float_t sc_pre[MAX_SUPERCLUSTERS];
  Float_t sc_raw[MAX_SUPERCLUSTERS];
  Int_t sc_nbc[MAX_SUPERCLUSTERS];
  Int_t sc_bcseedind[MAX_SUPERCLUSTERS];
  Int_t sc_bcind[MAX_SUPERCLUSTERS][MAX_SUPERCLUSTER_BASICCLUSTERS];
  Int_t sc_barrel[MAX_SUPERCLUSTERS];
  Float_t sc_2xN[MAX_SUPERCLUSTERS];
  Float_t sc_5xN[MAX_SUPERCLUSTERS];
  Float_t sc_sieie[MAX_SUPERCLUSTERS];
 
// BASIC CLUSTERS
  Int_t bc_n;
  Int_t bc_hybrid_n;
  Int_t bc_islbar_n;
  Int_t bc_islend_n;
  Int_t bc_nhits[MAX_BASICCLUSTERS];
  Int_t bc_type[MAX_BASICCLUSTERS];

  //Float_t bc_rook[MAX_BASICCLUSTERS];
  Float_t bc_s1[MAX_BASICCLUSTERS];
  Float_t bc_s4[MAX_BASICCLUSTERS];
  Float_t bc_s9[MAX_BASICCLUSTERS];
  Float_t bc_s25[MAX_BASICCLUSTERS];
  //Float_t bc_hoe[MAX_BASICCLUSTERS];
  //Float_t bc_radius[MAX_BASICCLUSTERS];
  //Float_t bc_z[MAX_BASICCLUSTERS];
  Float_t bc_sipip[MAX_BASICCLUSTERS];
  Float_t bc_sieie[MAX_BASICCLUSTERS];
  Float_t bc_sieip[MAX_BASICCLUSTERS];
  Float_t bc_chx[MAX_BASICCLUSTERS];
  
  Float_t bc_s1x5_0[MAX_BASICCLUSTERS];
  Float_t bc_s1x5_1[MAX_BASICCLUSTERS];
  Float_t bc_s1x5_2[MAX_BASICCLUSTERS];
  Float_t bc_s1x3_0[MAX_BASICCLUSTERS];
  Float_t bc_s1x3_1[MAX_BASICCLUSTERS];
  Float_t bc_s1x3_2[MAX_BASICCLUSTERS];
  Float_t bc_s5x1_0[MAX_BASICCLUSTERS];
  Float_t bc_s5x1_1[MAX_BASICCLUSTERS];
  Float_t bc_s5x1_2[MAX_BASICCLUSTERS];
  Float_t bc_s3x1_0[MAX_BASICCLUSTERS];
  Float_t bc_s3x1_1[MAX_BASICCLUSTERS];
  Float_t bc_s3x1_2[MAX_BASICCLUSTERS];
  Float_t bc_2x5_max[MAX_BASICCLUSTERS];
  Float_t bc_5x1_sam[MAX_BASICCLUSTERS];
  Int_t bc_seed[MAX_BASICCLUSTERS];
  
 private:
  const char* nome;
  GlobeCuts *gCUT;

// SUPER CLUSTERS
  edm::InputTag hybridSuperClusterColl; 
  edm::InputTag barrelSuperClusterColl; 
  edm::InputTag endcapSuperClusterColl; 

// BASIC CLUSTERS
  edm::InputTag barrelHybridClusterColl; 
  edm::InputTag barrelBasicClusterColl; 
  edm::InputTag endcapBasicClusterColl; 
  edm::InputTag barrelHybridClusterShapeColl; 
  edm::InputTag barrelBasicClusterShapeColl; 
  edm::InputTag endcapBasicClusterShapeColl; 
  edm::InputTag ecalHitEBColl;
  edm::InputTag ecalHitEEColl;

  int debug_level;
};


#endif
