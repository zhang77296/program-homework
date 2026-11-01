def check(product, a, b):
    s = str(product) + str(a) + str(b)
    if len(s) != 9:
        return False
    if '0' in s:
        return False
    return len(set(s)) == 9

res = []
# product 四位数：1000 ~ 9999
for p in range(1000, 10000):
    for a in range(1, int(p**0.5) + 1):
        if p % a == 0:
            b = p // a
            if check(p, a, b):
                res.append((p, a, b))

# 排序规则：先按乘积从小到大，乘积相同按a从小到大
res.sort(key=lambda t: (t[0], t[1]))
for p, a, b in res:
    print(f"{p} = {a} x {b}")