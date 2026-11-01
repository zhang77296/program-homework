L, R = map(int, input().split())
cnt = 0
for i in range(L, R + 1):
    cnt += str(i).count('2')
print(cnt)