#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

annotation = "/Users/cmdb/qbb2015/rawdata/samples.csv"
df = pd.read_csv(annotation, header=0, comment=None)

df.columns = ["sample", "sex", "stage"]

#print df
#Load the file /Users/cmdb/qbb2015/rawdata/samples.csv. Loop through these 16 samples and load the corresponding t_data.ctab file in /Users/cmdb/qbb2015/stringtie. Print out out the row for transcript FBtr0331261.


roi = df["sample"].str.contains("SRR072*")

#print roi
for filename in roi:
      if roi == True:
            print "Users/cmdb/qbb2015/stringtie/SRR072*/t_data.ctab"
            #open "Users/cmdb/qbb2015/stringtie/SRR072*/t_data.ctab"
            
      else:
            pass
      
     
  
  #   data = filename.split()
    #  if "sample" in data[0]
      
      