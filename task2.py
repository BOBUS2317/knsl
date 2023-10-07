def f2('x y z w')
for x in range(2):
   for y in range(2):
      for z in range(2):
         for w in range(2):
            if (not(y<=x) or (z<=w) or not(z))==False:
               print(x, y, z, w)

f2(1,2,3,4)
