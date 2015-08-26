#!/usr/bin/env python

import pandas as pd
#import matplotlib.pyplot as plt

annotation = "/Users/cmdb/qbb2015/rawdata/samples.csv"
df = pd.read_csv(annotation, header=0, comment=None)
#call = "/Users/cmdb/qbb2015/stringtie/SRR072*/t_data.ctab"

#df.columns = ["sample", "sex", "stage"]

#print df
#Load the file /Users/cmdb/qbb2015/rawdata/samples.csv. Loop through these 16 samples and load the corresponding t_data.ctab file in /Users/cmdb/qbb2015/stringtie. Print out out the row for transcript FBtr0331261.

#roi = df["sample"].str.contains("SRR072*")

#print roi
count = 0
for filename in df["sample"]:
      temp_loc = "/Users/cmdb/qbb2015/stringtie/"+filename+"/t_data.ctab"
      file = open (str(temp_loc))
      print filename
      for line in file:
            if "FBtr0331261" in line:
                  print line
                  count +=1
            else:
                  pass
print count
            #print "This is less frustrating"
           #  call
      #print filename
      #print "okay"





#print roi

#for filename in roi:
 #     print filename
  #    print "odd"

#for filename in roi:
 #     if filename.endswith(89*):
  #          print "choose"
   #   elif filename.endswith(9**):
    #        print "choose"
     # else:
      #      pass

      # "Users/cmdb/qbb2015/stringtie/SRR072*/t_data.ctab"
            #open "Users/cmdb/qbb2015/stringtie/SRR072*/t_data.ctab"
            
   
   #   else:
    
    #        pass
      
     
  
  #   data = filename.split()
    #  if "sample" in data[0]
      
      