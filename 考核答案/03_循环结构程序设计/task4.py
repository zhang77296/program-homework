T = int(input())
for _ in range(T):
    n = int(input())
    mid = n // 2
    for i in range(n):
        d = abs(i - mid)
        space = d
        star = n - 2 * d
        print(" " * space + "*" * star)