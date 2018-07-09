from sys import *
from random import *
import numpy

n = int(argv[1])
ave = []
for _ in range(n):
    ave.append(uniform(-1, 1))
    print("%.4f" % ave[-1])
print("Average of %d random numbers: %.4f" % (n, numpy.mean(ave)))