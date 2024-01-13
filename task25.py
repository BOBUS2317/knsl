def f251():
    for i in range(2024,10**10,2024):
        num=str(i)
        if fnmatch.fnmatch(num, "1?2157*4") == True:
            print(i,i//2024)
f251()
f252()
import re
def f25():
    for i in range(2024,10**10,2024):
        if re.match("^1.2157.*4$",str(i)):
            print(i,i//2024)
f252()
