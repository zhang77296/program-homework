n=int(input())
num=1
for i in range(1,n+1):
    line=""
    for j in range(i):
        line+=f"{num:4d}"
        num+=1
    print(line)