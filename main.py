import cmath
import math
x = float(input("Input number to find it's square root: " ))
#calculates root depending on whether it's complex or real
def sqrt(x):
  if x < 0:
    crt = cmath.sqrt(x)
    print(crt)
  if x >= 0:
    rt = math.sqrt(x)
    #truncate if number is perfect square
    if int(rt+0.5)**2 == x:
      rtint = math.trunc(rt)
      print(rtint)
    else: 
      print(rt)
sqrt(x)
