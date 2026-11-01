x,y=map(int,input().split())
print(sum(1 for i in range(x,y+1)
if sum(map(int,str(i)))%5==0))