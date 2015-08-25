#!/usr/bin/env python

import pandas as pd #pd use package

annotation = "/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"

df = pd.read_table(annotation, comment='#', header=None) # df - data frame

#print df
#print df.head()

#print df.describe()
#print df.info()

#print "\nThis is what happens with [1:5]"

#print df[1:5] #print 1 through 5, non inclusive 5 not included

#print "\nThis is what happens with [0:5]" #forwardslash adds space

#print df [0:5]

#print "\nShow rows 10 through 15 inclusive pertaining"

#print df[9:15]


#print "\n show rows 20-25"

#print df[19:25]

#print df.info()
df.columns = ["chromosome", "database", "type", "start","end", "score", "strand", "frame", "attributes"] #attribute not function so no parentheses at df.columns

#print df.info

#print df.sort(columns="type", ascending=False)

#subset chromosome start and end of coloumns
#print df[["chromosome","start", "end"]]


#print df["start"][9:15]

#print df.shape
df2 = df["start"]
#print df2.shape

df2.to_csv("startColumn.txt", sep='\t', index=False)
print df.shape
roi = df["start"] < 10
print roi.shape
print df[roi]