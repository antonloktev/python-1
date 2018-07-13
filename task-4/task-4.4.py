from sys import *
from math import *
import numpy


i = 1;
while 1:
    try:
      if float(argv[i]) > 0:
        print("ln(%g)" % float(argv[i]), "=", log(float(argv[i])))
      else:
        print("ln(%g)" % float(argv[i]), "is illegal")
    except IndexError:
        break
    i = i + 1;