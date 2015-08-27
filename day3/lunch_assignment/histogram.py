#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

filename = ("/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab")


SRR893_table = pd.read_table(filename)

FPKM = []

for data in SRR893_table["FPKM"]:
      
      if np.log(data) > 0.0:
            
            FPKM.append(np.log(data))
      
      else:
            pass
            
plt.figure()
plt.hist(FPKM)
plt.title("log.FPKM for SRR072893")
plt.xlabel("log.FPKM")
plt.ylabel("Frequency")
plt.savefig("SRR072893_FPKM_histogram.png")