from sys import *
from math import *
import numpy

for n in argv[1:]:
    if float(n) > 0:
        print("ln(%g" % float(n), " = ", log(float(n)))
    else:
        print("ln(%g" % float(n), " is illegal ")