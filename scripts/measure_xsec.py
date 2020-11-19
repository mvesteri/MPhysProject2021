#!/usr/bin/env python
from ROOT import gROOT
gROOT.SetBatch(True)
import ROOT
import json

file_path = "/storage/epp2/phshgg/DVTuples__v23/5TeV_2017_32_Down_EW.root"

ch = ROOT.TChain('Z/DecayTree')
ch.Add(file_path)

count = ch.GetEntries("Z_M > 60.e3 && Z_M < 120.e3 && mup_PT > 20.e3 && mum_PT > 20.e3 && mup_ETA > 2 && mup_ETA < 4.5 && mum_ETA > 2 && mum_ETA < 4.5")

with open('data.txt') as json_file:
    data = json.load(json_file)

lumi = data["luminosity"]
lumi_err = data["luminosity_err"]
trig_eff = data["trigger_efficiency"]

xsec = count/(lumi*trig_eff)
xsec_err = xsec - count/((lumi+lumi_err)*trig_eff)

print('Z Count = {}'.format(count))
print('Z Cross Section (pb) = {}'.format(xsec))
print('XSec Error (pb) = {}'.format(xsec_err))