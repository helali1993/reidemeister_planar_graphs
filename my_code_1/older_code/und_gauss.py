import pyknotid.representations as rep_
import sys


#gc = rep_.GaussCode('1-c,2+a,3-c,4+c,2-a,1+a,4-a,3+c') # knot 4_1

# Non-Alternating knot that turned out to be 4_1 through R2.
# Cool example to use in report and presentation. 
# gc = rep_.GaussCode('1-c,2-a,3+c,4-c,2+a,5-a,6+a,1+c,4+c,3-c,5+a,6-a')

gc = rep_.GaussCode('1-c,2+c,4+c,4-c,3-c,1+c,2-c,3+c')

rep = rep_.Representation(gc)

k = rep.space_curve(bool=False)

k.plot()

print(k.identify())

input()

sys.exit()