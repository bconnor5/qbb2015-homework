#!/usr/bin/env python

from __future__ import division #change division operator to include float number USE!!! OFTENN
import numpy as np
import sys
from matplotlib_venn import venn3, venn3_circles # dont forget second input!
import matplotlib.pyplot as plt

import chrmloc_class

arr = chrmloc_class.Chrmloc( fname = sys.argv[1])


#need to copy array of length file before inputs so same array not continously overwritten @ line 26

CTCF = arr.copy() 
BEAF = arr.copy()
SuHW = arr.copy()

CTCF.set_bits_from_file( sys.argv[2])
BEAF.set_bits_from_file( sys.argv[3])
SuHW.set_bits_from_file( sys.argv[4])

Union = CTCF.union( BEAF.union(SuHW) )



arr_CTCF = CTCF
arr_BEAF = BEAF
arr_SuHW = SuHW

count_Abc = 0
count_aBc = 0
count_abC = 0
count_ABc = 0
count_AbC = 0
count_aBC = 0
count_ABC = 0

total_arr = 0
total_arr_CTCF = 0
total_arr_BEAF = 0
total_arr_SuHW = 0

for filename in sys.argv[2:]:
      for line in open (filename):
          fields = line.split()
      #parse fields
          chrom = fields[0]
          start = int( fields[1] )
          end = int( fields[2] )
      #get slice
          sl = arr.arrays[chrom][start:end]
          total_arr += 1
         
          sl_arr_CTCF = arr_CTCF.arrays[chrom][start:end]
          total_arr_CTCF += 1
          
          sl_arr_BEAF = arr_BEAF.arrays[chrom][start:end]
          total_arr_BEAF += 1
          
          sl_arr_SuHW = arr_SuHW.arrays[chrom][start:end]
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
plt.title("CTCF BEAF SuHW Union Venn Diagram")   #A      B           AB          C           AC          BC    ABC - order of ven input for 3 comparison              
v = venn3(subsets = (count_Abc, count_aBc, count_ABc, count_abC, count_AbC, count_aBC, count_ABC), set_labels = ("CTCF", "BEAF", "SuHW"))       
c = venn3_circles(subsets=(count_Abc, count_aBc, count_ABc, count_abC, count_AbC, count_aBC, count_ABC))         
plt.savefig("union_venn2.png")
#print "Total arr:", total_arr, "total_arr_CTCF:", total_arr_CTCF, "Count CTCF:", count_Abc, "Total BEAF:", total_arr_BEAF, "Count BEAF:", count_aBc, "Total SuHW:", total_arr_SuHW, "Count SuHW:", count_abC 
