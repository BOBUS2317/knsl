f = open('27A_2724.txt')
n = int(f.readline())
k = [0]*131
for i in range(n):
  × = int(f.readline()) 
  k[x%131]+=1
count = 0
count += k[0]*(k[0]-1)//2
for i in range(1,65+1): count+=k[i]*k[131-i]
print(count)
