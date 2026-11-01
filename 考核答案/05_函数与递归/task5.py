import sys
data=sys.stdin.read().split()
t=int(data[0])
res=[]
for i in range(t):
    a=int(data[1+2*i])
    b=int(data[2+2*i])
    res.append(str(a*b))
print("\n".join(res))