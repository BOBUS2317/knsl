def f16():
    #sys.setrecursionlimit(2500)
    i1=i2=1
    for x1 in range(1,2024):
        i1=i1*x1
    for x2 in range(1,2021):
        i2=i2*x2
    print(i1/i2)

f16()
