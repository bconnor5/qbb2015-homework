#!/usr/bin/env python

from __future__ import division

import pandas as pd 
import sys
import copy



import chrmloc_class


arr = chrmloc_class.Chrmloc( fname=sys.argv[1] )

ctcf = arr.copy()
beaf = arr.copy()

ctcf.set_bits_from_file( sys.argv[2] )
beaf.set_bits_from_file( sys.argv[3] )

A_notB = beaf.intersect( ctcf.complement() )
location = A_notB.bed()

print location