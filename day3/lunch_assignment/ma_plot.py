#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

SRR893 = ("~/qbb2015/stringtie/SRR072893/t_data.ctab")

SRR905 = ("~/qbb2015/stringtie/SRR072905/t_data.ctab")

SRR893_table = pd.read_table(SRR893)
SRR905_table = pd.read_table(SRR905)

R = SRR893_table["FPKM"] 

G = SRR905_table["FPKM"]

r = R[R > 0]
g = G[G > 0]


m = np.log2(r/g)  #log base 2 r/g binary logarithm: difference between log intensitites

a = .5 * np.log2(r * g) # average log intensity of dot in plot

plt.figure()
plt.title("MA Plot: SRR072893 vs SRR07905")
plt.scatter(a,m)
plt.xlabel("A")
plt.ylabel("M")
plt.savefig("MA_Plot_SRR893_vs_SRR905.png")