def f24():
    with open('24.txt') as f:
       let=f.readline()
       count,maximum=0,0
       #text=''
       delta=0
       for i in range(len(let)-1):
          if (let[i]=='C' or let[i]=='D' or let[i]=='F') and (let[i+1]=='A' or let[i+1]=='O'):
             delta=0
             #text=text+let[i]+let[i+1]
             count+=1
             maximum=max(count,maximum)
          else: delta+=1
          if delta==2:
             count=0
             #text=''
    print(maximum)

f23()
