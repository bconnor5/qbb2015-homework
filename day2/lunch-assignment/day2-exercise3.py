#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/day2-lunch/SRR072893.sam"

f = open ( filename )

single_align_count = 0
for line in f:
      if "@" in line:
            pass
      
      elif "NM:i:1" in line:
            
           single_align_count += 1
      
      else:
            pass
      

print "Perfect Match Count: ", single_align_count