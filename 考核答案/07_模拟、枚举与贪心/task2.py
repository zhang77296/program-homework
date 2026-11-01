import sys
 
mid = {
    (1, 3): 2, (3, 1): 2,
    (4, 6): 5, (6, 4): 5,
    (7, 9): 8, (9, 7): 8,
    (1, 7): 4, (7, 1): 4,
    (2, 8): 5, (8, 2): 5,
    (3, 9): 6, (9, 3): 6,
    (1, 9): 5, (9, 1): 5,
    (3, 7): 5, (7, 3): 5,
}
 
def check(s):
    used = set()
    for i, ch in enumerate(s):
        d = int(ch)
        if d in used:                       # 重复
            return False
        if i > 0:
            a, b = int(s[i - 1]), d
            m = mid.get((a, b))
            if m is not None and m not in used:   # 中间点未用过
                return False
        used.add(d)
    return True
 
for line in sys.stdin:
    s = line.strip()
    if s:
        print("YES" if check(s) else "NO")