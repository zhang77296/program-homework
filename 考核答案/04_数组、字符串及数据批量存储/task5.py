n = int(input())
a = list(map(int, input().split()))
 
last = a[-1]
 
if last == 0:
    print("UP")
elif last == 15:
    print("DOWN")
else:
    if n == 1:
        print("-1")
    elif last > a[-2]:
        print("UP")
    else:
        print("DOWN")