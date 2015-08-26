#!/usr/bin/env python

import pandas as pd 
import matplotlib.pyplot as plt

annotation = "/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"

df = pd.read_table(annotation, comment="#", header=None)

df.columns = ["chromosome", "database", "type", "start","end", "score", "strand", "frame", "attributes"]




roi = df["attributes"].str.contains("Sxl")
print df[roi].shape

roi2 = df["type"].str.contains("transcript")
#print df2.shape

print df[roi][roi2]

#roi = df["attributes"].str.contains("Sxl")
#df2 = df[roi]
#roi2= df["type"].str.contains("transcript")
#df3 = df2[roi2]
#col = df3["start"]

plt.figure()
plt.title("Sxl , Transcripts")
plt.plot(df[roi][roi2]["start"])
plt.ylabel("Start Position")
plt.xlabel("gene")
plt.savefig("Sxl_Trascript_Loci")