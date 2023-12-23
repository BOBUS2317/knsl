def f16():
    #sys.setrecursionlimit(2500)
    i1=i2=1
    for x1 in range(1,2024):
        i1=i1*x1
    for x2 in range(1,2021):
        i2=i2*x2
    print(i1/i2)

f16()

from math import factorial
import sys 
sys.setrecursionlimit(2500)
def f1(n):
    if n>2024: return n
    if n<=2024: return n*f1(n+1)
print(f1(2022)/f1(2024))

def f2(n):
    if n==1: return 1
    return n*f2(n-1)
print(f2(10))
