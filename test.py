import math
instr = input("enter the value")
temp = set()
outarr = []

for i in range(0,len(instr)):
    for j in range(i,len(instr)):
        substr = int(instr[i:j+1])
        temp.add(substr)

temp = sorted(list(temp))
for i in temp:
    for j in range(0,int(math.sqrt(i))+1):
        print(j)
#        if(i == j*(j+1)):
 #           outarr.append(i)
#print(outarr)
        
