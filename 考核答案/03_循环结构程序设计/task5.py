while True:
    try:
        n = int(input())
        # 上半部分
        for i in range(n+1):
            print("  " * (n - i) + "*" * (i + 1))
        # 下半部分
        for i in range(n):
            print("  " * (i + 1) + "*" * (n - i))
    except EOFError:
        break