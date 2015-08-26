#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt


metadata = pd.read_csv("~/qbb2015/rawdata/samples.csv")
Sxl_f = []
Sxl_m = []

dev_stage = {}

rep_data = pd.read_csv("~/qbb2015/rawdata/replicates.csv")

reps = {}


for i, data in metadata.iterrows():
      if data ["stage"] in ["10", "11", "12", "13", "14A", "14B", "14C", "14D"]:
            if data["stage"] not in dev_stage:
                  dev_stage[data["stage"]] = 1
            else :
                  dev_stage[data["stage"]] += 1

for sample in metadata[metadata["sex"] == "female"]["sample"]: #second bracket pulls out sample column of females denoted by first embedded metadata command
    df = pd.read_table("~/qbb2015/stringtie/" + sample + "/t_data.ctab")  
    roi = df["t_name"].str.contains("FBtr0331261")
    df[roi]["FPKM"].values #will give associated value instead of character string      
    Sxl_f.append(df[roi]["FPKM"].values)
    
for sample2 in metadata[metadata["sex"] == "male"]["sample"]:
      df2 = pd.read_table("~/qbb2015/stringtie/" + sample2 + "/t_data.ctab")
      roi2 = df2["t_name"].str.contains("FBtr0331261")
      df2[roi2]["FPKM"].values
      Sxl_m.append(df2[roi2]["FPKM"].values)
      
for i, replicates in rep_data.iterrows():
      if replicates["stage"] in ["14A", "14B", "14C", "14D"]:
            if data["stage"] not in reps:
                  reps[replicates["stage"]] = 1
            else:
                  reps[replicates["stage"]] += 1
      
      
print Sxl_m
print Sxl_f      
      
plt.figure()
plt.plot(Sxl_f, 'r') 
plt.plot(Sxl_m, 'b')
plt.plot(reps, 'g')
plt.title("Sxl")
plt.xlabel("Developmental Stage")
plt.ylabel("mRNA abundance (RPKM)")
plt.ylim(0,300)
plt.xticks(range(len(dev_stage)),["10", "11", "12", "13", "14A", "14B", "14C", "14D"])
plt.legend(['female', 'male'])
plt.savefig("timecourse.png")


#df = pd.read_table("~/qbb2015/stringtie/SRR072893/t_data.ctab")

#df2 = pd.read_table("~/qbb2015/stringtie/SRR072915/t_data.ctab")

#plt.figure()
#plt.scatter(df["FPKM"], df2["FPKM"])
#plt.xlabel("893 - male 10")
#plt.ylabel("915 - female 14D")
#plt.savefig("scatterplot.png") #represent comparison between abundance of transcript isoform between male and female animal

#chrom_count = {} #dictionary called chrom_count

#for i, line in df.iterrows(): #iterrows() will pull out the first row and describe (df alone gives column header)
      #print line["chr"]
 #     if line ["chr"] in ["2L","2R","3L","3R", "X","Y"]:
  #          if line ["chr"] not in chrom_count:
   #             chrom_count[line["chr"]] = 1
    #        else:
     #           chrom_count[line["chr"]] += 1

#print chrom_count.values()
#print chrom_count.keys()

#plt.figure()
#plt.bar(range(len(chrom_count)))
#plt.xticks(range(len(chrom_count)), chrom_count.keys())
#plt.savefig("barplot.png")

