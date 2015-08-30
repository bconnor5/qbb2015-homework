#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/day2-lunch/SRR072893.sam"

f = open ( filename )

line_counter = 0



for line in f:
      if not line.startswith("@"):
            fields = line.split()
            Chrm = fields[2]
            pos = fields[3]
            if Chrm == "2L" and int(pos) >10000 and int(pos) < 20000:
                  
                  line_counter += 1
            else:
                  break
                  
print line_counter