n,k,m=map(int,input().split())
people=list(range(n))
idx=k
while len(people)>1:
    idx=(idx+m-1)%len(people)
    people.pop(idx)
print(people[0])