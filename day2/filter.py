#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"

f = open ( filename )
name_counts = {}

#line_count=0 #alternatively use enumerate (f) as " for line_count, data in enumerate (f) "
#for line in f:
    #fields = line.split() 
        
    #if "tRNA" in fields[9]:
     #   print line, #comma suppresses new line
 #   if line_count <= 10:
  #      pass
   # elif line_count <= 15:
    #    print line,
    #else:
     #     break
    #line_count += 1


#alternate method

#for line_count, line in enumerate(f):
 #     if line_count <=10:
  #          pass
   #   elif line_count <=15:
    #        print line
     # else:
      #
      
      #      break
for line_count, data in enumerate(f):
    fields = data.split()
    gene_name = fields[9]
    if gene_name not in name_counts:
        name_counts[ gene_name ] = 1
    else: 
        name_counts[ gene_name ] += 1
                
      # iterate key, value pairs from name counts dictionary
for key, value in name_counts.iteritems():
      print key, value