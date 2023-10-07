def f8():
    from itertools import product
    k=0
    n='16 36 56 76 61 63 65 67'
    nn=n.split()
    nums=product('01234567',repeat=5)
    for n in nums:
        numb=''.join(n)
        if numb.count('6')==1 and numb[0]!='0':
            if all(not(x in numb) for x in nn):
                k+=1
    print(k)

f8()
