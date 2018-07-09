from sys import *
from math import *
import numpy

i = 1
while i < len(argv):
    if float(argv[i]) > 0:
        print("ln(%g" % float(argv[i]), " = ", log(float(argv[i])))
    else:
        print("ln(%g" % float(argv[i]), " is illegal ")
    i += 1
