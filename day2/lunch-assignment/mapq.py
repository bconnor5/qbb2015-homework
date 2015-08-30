#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/day2-lunch/SRR072893.sam"

f = open ( filename )

line_counter = 0

mapq_total = 0

for line in f:
      if "@" in line:
            
            pass
            
      else:
            
            fields = line.split()
            mapq = fields[4]
            mapq_value = float(mapq)
            mapq_total = mapq_total + mapq_value
            
            line_counter += 1
      
print "Average MAPQ Score: ", mapq_total / line_counter                  