def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        a = list(map(int, input().split()))
        mx = max(a)
        mn = min(a)
        r = mx - mn
        avg = sum(a) / n
        s = 0.0
        for x in a:
            s += (x - avg) ** 2
        var = s / n
        print(f"{r} {var:.3f}")

if __name__ == "__main__":
    main()