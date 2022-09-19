import cmath
import math
x = float(input("Input number to find its square root: "))  # you can use \n if you want to add a linebreak

def sqrt(x):
  if x < 0:
    crt = cmath.sqrt(x)
    print(crt)
  elif x > 0 or x == 0 :  # i think x >= 0 does both
    rt = math.sqrt(x)
    print(rt)

sqrt(x)
