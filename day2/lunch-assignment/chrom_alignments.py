#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/day2-lunch/SRR072893.sam"

f = open ( filename )


Chrm_count = {"2L":0, "2R":0, "3L":0, "3R":0, "4":0, "X":0}



for i, line in enumerate(f):
       
             fields = line.split()
             
             Chrm = fields[2]
             
             if Chrm in Chrm_count:
                   Chrm_count[Chrm] += 1
            
             else:
                  pass
for key, value in Chrm_count.iteritems(): #iterate to print all items
      print key, value
             