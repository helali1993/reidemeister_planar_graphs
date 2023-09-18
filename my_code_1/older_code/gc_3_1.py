import pyknotid.spacecurves as sp
import pyknotid.make as mk
from pyknotid.make import trefoil
import numpy as np
import sys

k = sp.Knot(trefoil())

print(k.gauss_code())