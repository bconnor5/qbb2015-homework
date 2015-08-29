#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

fname = open( sys.argv[1] )


E_val = []

Bit_count = []




for line in fname:
      fields = line.split()
      E = fields[10]
      bit= fields[11]
      E_val.append(float(E))
      Bit_count.append(float(bit))
      
#print E_val
#print Bit_count

plt.figure()
plt.hist(E_val)
plt.title("E Value")   
plt.xlabel("E value")
plt.ylabel("Frequency")
plt.savefig("E_val.png")

plt.figure()
plt.hist(Bit_count, bins=200, range=(0,200))
plt.title("Bit Score")   
plt.xlabel("Bit Score")
plt.ylabel("Frequency")
plt.xticks
plt.savefig("bit_count.png")

plt.figure()
plt.scatter(np.log(Bit_count), np.log(E_val))
plt.title("Bit Scores vs. E_value")
plt.xlabel("log.Bit Score")
plt.ylabel("log.E Value")
plt.savefig("Scatter_ebits")
            
          
      