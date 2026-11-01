ch = input().strip()
n = ord(ch) - ord('A') + 1
for i in range(n):
    s = ""
    # 前置空格
    s += " " * (n - 1 - i)
    # 正向 A -> ...
    for k in range(i+1):
        s += chr(ord('A') + k)
    # 反向倒回去
    for k in range(i-1, -1, -1):
        s += chr(ord('A') + k)
    print(s)