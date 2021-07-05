"""Svago.
"""



import  ROOT
import numpy


#Include the header file
ROOT.gInterpreter.Declare('#include "include/prova.h"')


# Enable multi-threading
ROOT.gInterpreter.ProcessLine("ROOT::EnableImplicitMT()")


#Python functions



timer = ROOT.TStopwatch()

if __name__ == "__main__":

    data_path = "root://eospublic.cern.ch//eos/root-eos/cms_opendata_2012_nanoaod/"
    rdf = ROOT.RDataFrame("Events", (data_path + f for f in ["Run2012B_DoubleMuParked.root",\
    "Run2012C_DoubleMuParked.root", "Run2012B_DoubleElectron.root", \
    "Run2012C_DoubleElectron.root"]))

    timer.Start()
    rdf_4e = rdf.Filter("nElectron >= 4", "First selection with at least 4 electrons").Histo1D(("Prova", "", 500, 0, 500), "Electron_pt")
    h = rdf_4e.GetValue()
    h.DrawCopy("PE1")
    timer.Stop()
    print(timer.RealTime())
    
    timer.Start()
    temp = rdf.AsNumpy(columns=["nElectron","Electron_pt"]) 
    timer.Stop()
    print(timer.RealTime())








    