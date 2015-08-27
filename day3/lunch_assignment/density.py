#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

filename = ("/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab")


table = pd.read_table(filename)

#FPKM = []

#for data in SRR893_table["FPKM"]:
      
 #     if data > 0.0:
            
  #          FPKM.append(data)
      
   #   else:
    #        pass
            
#log = np.log(FPKM)            


table_filterzero = table[table["FPKM"] != 0]

log = np.log(table_filterzero["FPKM"])




plt.figure()
log.plot(kind='kde')
plt.title("Kernel Density Estimation of SRR072893 FPKM")
plt.xlabel("log.FPKM")
plt.ylabel("Frequency")
plt.savefig("Kernel_Density_Est.png")