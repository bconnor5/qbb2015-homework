#!/usr/bin/env python

from __future__ import division #change division operator to include float number USE!!! OFTENN
import numpy as np
import sys
from matplotlib_venn import venn3, venn3_circles
import matplotlib.pyplot as plt

def arrays_from_len_file (fname):
      arrays = {}
      for line in open (fname):
            fields = line.split()
            name = fields[0]
            size = int( fields[1] )
            arrays[name] = np.zeros(size, dtype=bool)
      return arrays



def set_bits_from_file(arrays, fname):
      for line in open( fname ):
            fields = line.split()
            #Parse fields
            chrom = fields[0]
            start = int( fields[1] )
            end = int ( fields[2] )  
            arrays[ chrom ][ start : end ] = 1
            

arr = arrays_from_len_file( sys.argv[1])
arr_CTCF = arrays_from_len_file( sys.argv[1] )
arr_BEAF = arrays_from_len_file( sys.argv[1] )
arr_SuHW = arrays_from_len_file( sys.argv[1] )

set_bits_from_file( arr_CTCF, sys.argv[2])
set_bits_from_file( arr_BEAF, sys.argv[3])
set_bits_from_file( arr_SuHW, sys.argv[4])

""""""""""""""""""""""""""""""""

total_arr = 0 
total_arr_CTCF = 0
total_arr_BEAF = 0
total_arr_SuHW = 0

count_Abc = 0
count_aBc = 0
count_abC = 0
count_ABc = 0
count_AbC = 0
count_aBC = 0
count_ABC = 0
#twentyper_overlap = 0

for filename in sys.argv[2:]:
      for line in open (filename):
          fields = line.split()
      #parse fields
          chrom = fields[0]
          start = int( fields[1] )
          end = int( fields[2] )
      #get slice
          sl = arr[chrom][start:end]
          total_arr += 1
         
          sl_arr_CTCF = arr_CTCF[chrom][start:end]
          total_arr_CTCF += 1
          
          sl_arr_BEAF = arr_BEAF[chrom][start:end]
          total_arr_BEAF += 1
          
          sl_arr_SuHW = arr_SuHW[chrom][start:end]
          total_arr_SuHW += 1
         
          
          if sl_arr_CTCF.any() and sl_arr_BEAF.any() and sl_arr_SuHW.any():
                
                count_ABC += 1   #all three
                
          elif sl_arr_CTCF.any() and sl_arr_BEAF.any() and not sl_arr_SuHW.any():
                
                count_ABc += 1 # just CTCF and BEAF
                
          elif sl_arr_CTCF.any() and sl_arr_SuHW.any() and not sl_arr_BEAF.any():
                
                count_AbC += 1 # just CTCF and SuHW
               
          elif sl_arr_SuHW.any() and sl_arr_BEAF.any() and not sl_arr_CTCF.any():
                
                count_aBC += 1  # justSuHW and BEAF      
          
          
          elif sl_arr_CTCF.any() and not (sl_arr_BEAF.any() or sl_arr_SuHW.any()):
                
                count_Abc += 1                      #CTCF only
          
          elif sl_arr_BEAF.any() and not (sl_arr_CTCF.any() or sl_arr_SuHW.any()):
                
                count_aBc += 1  
          
          elif sl_arr_SuHW.any() and not (sl_arr_CTCF.any() or sl_arr_BEAF.any()):                      
                
                count_abC += 1
      
          else:
                pass                            
                
plt.figure()
plt.title("Venn Diagram")                
v = venn3(subsets = (count_Abc, count_aBc, count_ABc, count_abC, count_AbC, count_aBC, count_ABC), set_labels = ("CTCF", "BEAF", "SuHW"))       
c = venn3_circles(subsets=(count_Abc, count_aBc, count_ABc, count_abC, count_AbC, count_aBC, count_ABC))         
plt.savefig("overlaps.png")
#print "Total arr:", total_arr, "total_arr_CTCF:", total_arr_CTCF, "Count CTCF:", count_Abc, "Total BEAF:", total_arr_BEAF, "Count BEAF:", count_aBc, "Total SuHW:", total_arr_SuHW, "Count SuHW:", count_abC 
 

 


      
      #20 % overlap
 #         twentyper_arr += (np.sum( sl_arr ) / len( sl_arr ) > 0.2 )
  #        twentyper_arr2 += (np.sum(sl_arr2) / len( sl_arr2) > 0.2 )
      
#print "%d vs %d - Total: %d 20 percent overlap: %d" % (x, i, total, twentyper_overlap) 


















#for x in range(2,5):
 #     set_bits_from_file(arrays, sys.argv[x])
  #          
   #   for i in range (2,5):
    #        for line in open (sys.argv[i]):
     #             fields = line.split()
      #            chrom = fields[0]
       #           start = int( fields[1] )
        #          end = int ( fields[2] )
            #Get slice
         #         sl = arrays[chrom][start:end]
          #        total += 1 #track total number of lines
           #      any_overlap += sl.any()
            #      all_overlap += sl.all()
      #20 % overlap
             #     twentyper_overlap += (np.sum( sl ) / len( sl ) > 0.2 )
      
            #print "%d vs %d - Total: %d, Any overlap: %d, All overlap %d 20 percent overlap: %d" % (x, i, total, any_overlap, all_overlap, twentyper_overlap) # %d decimal %s string %f float number
            
      
                  
          