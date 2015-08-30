#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/day2-lunch/SRR072893.sam"

f = open ( filename )

perfect_match_count = 0
for line in f:
      if "@" in line:
            pass
      
      elif "NM:i:0" in line:
            
            perfect_match_count += 1
            
      else:
            pass
      
   

print "Perfect Match Count: ", perfect_match_count