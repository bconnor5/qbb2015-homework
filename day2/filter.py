#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"

f = open ( filename )

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

for line_count, line in enumerate(f):
      if line_count <=10:
            pass
      elif line_count <=15:
            print line
      else:
            break