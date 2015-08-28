#!/usr/bin/env python

import sys
import pandas as pd

fname = open( sys.argv[1] )
 

 
while True:

      
      
      line = fname.readline()     
      
      if not line:
           
            break
      
      
      if line.startswith(">"):
            
            print line
            
      if line.startswith(" Identities"):
            
            print line
            
      #else:
       #     break
      

            
