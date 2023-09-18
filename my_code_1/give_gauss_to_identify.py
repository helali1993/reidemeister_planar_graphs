'''
We use this file to make sure our creations, our certain results
are correct by calculating manually the Gauss Code and checking if it 
gives us the expected knot
'''

import pyknotid.representations as rep_
import numpy as np
import sys
import pyknotid.make as mk
from pyknotid.catalogue import get_knot

gc = rep_.GaussCode("1+a,2-a,3+a,4-c,2+a,1-a,5+a,5-a,4+c,3-c")
rep = rep_.Representation(gc)

k = rep.space_curve(bool=False)


print(k.identify())
print(gc.mirrored())

# Print Gauss code of a knot in catalouge
# j = get_knot('3_1').space_curve()
#
# print(j.gauss_code())




