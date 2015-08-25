#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/day2-lunch/SRR072893.sam"

f = open( filename )

line_count = 0
for line in f:
      if "@" in line:
            pass
      else:
            line_count += 1
      
print line_count
#for line_count, data in enumerate(f):
 #   fields = data.split()
  #  gene_name = fields[9]
   # if gene_name not in name_counts:
    #    name_counts[ gene_name ] = 1
   # else: 
    #    name_counts[ gene_name ] += 1
                
      # iterate key, value pairs from name counts dictionary
#for key, value in name_counts.iteritems():
     # print key, value