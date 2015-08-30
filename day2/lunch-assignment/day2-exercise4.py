#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/day2-lunch/SRR072893.sam"

f = open ( filename )

line_count = 0

for line in f:
      if "@" not in line:
            if line_count <= 10:
                  Chrm = line.split()
                  
                  print "Chromosome: ", Chrm[2]
                  line_count += 1
                  
            else:
                  break
      