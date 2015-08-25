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

df2 = df[roi]["start"][roi2]

#roi = df["attributes"].str.contains("Sxl")
#df2 = df[roi]
#roi2= df["type"].str.contains("transcript")
#df3 = df2[roi2]
#col = df3["start"]

plt.figure()
plt.title("Sxl Transcripts")
plt.plot(df[roi]["start"])
plt.ylabel("Start Position")
plt.xlabel("Sxl Transcript locus")
plt.savefig("Sxl Trascript Loci")