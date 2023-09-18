'''
We use this file to make sure our creations, our certain results
are correct by calculating manually the Gauss Code and checking if it 
gives us the expected knot
'''

import pyknotid.representations as rep_
import numpy as np
import sys
import pyknotid.make as mk

gc = rep_.GaussCode("1+c,2-c,3-c,6-a,7-a,8-c,6+c,9+c,2+C,0+c,0-c,4-c,5-a,1-c,8+c,7+a,9-c,3+c.4+c,5+a")
rep = rep_.Representation(gc)

k = rep.space_curve(bool=False)
# k.plot()

print(k.identify())




