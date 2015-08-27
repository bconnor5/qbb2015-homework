#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

metadata = pd.read_csv("~/qbb2015/rawdata/samples.csv")

rep_metadata = pd.read_csv("~/qbb2015/rawdata/replicates.csv")

Sxl_f = []
Sxl_i_f = []

Sxl_m = []
Sxl_i_m = []

Sxl_r_f = []
Sxl_r_i_f = []

Sxl_r_m = []
Sxl_r_i_m = []

xbin = {"10":0, "11":1, "12":2, "13":3, "14A":4, "14B":5, "14C":6, "14D":7}

for i, data in metadata.iterrows():
      temp_ctab = pd.read_table("~/qbb2015/stringtie/%s/t_data.ctab" %(data["sample"]))
      
      if data["sex"] == "female":
            Sxl_f.append(temp_ctab[temp_ctab["t_name"].str.contains("FBtr0331261")]["FPKM"].values)
            Sxl_i_f.append(xbin[data["stage"]])
      else:
            Sxl_m.append(temp_ctab[temp_ctab["t_name"].str.contains("FBtr0331261")]["FPKM"].values)
            Sxl_i_m.append(xbin[data["stage"]])
            
for i, data in rep_metadata.iterrows():
      temp_ctab = pd.read_table("~/qbb2015/stringtie/%s/t_data.ctab" %(data["sample"]))
      
      if data ["sex"] == "female":
            Sxl_r_f.append(temp_ctab[temp_ctab["t_name"].str.contains("FBtr0331261")]["FPKM"].values)
            Sxl_r_i_f.append(xbin[data["stage"]])
      else:
            Sxl_r_m.append(temp_ctab[temp_ctab["t_name"].str.contains("FBtr0331261")]["FPKM"].values)
            Sxl_r_i_m.append(xbin[data["stage"]])
            
plt.figure()
plt.title("Sxl")
plt.xlabel("Developmental Stage")
plt.ylabel("mRNA Abundance (RPKM)")
plt.plot(Sxl_i_f, Sxl_f, 'r')
plt.plot(Sxl_i_m, Sxl_m, 'b')
plt.plot(Sxl_r_i_f, Sxl_r_f, 'ro')
plt.plot(Sxl_r_i_m, Sxl_r_m, 'bo')
plt.legend(["Female","Male","Female Replicates","Male Replicates"],"best")
plt.xticks(xbin.values(), xbin.keys())
plt.savefig("timecourse.png")
