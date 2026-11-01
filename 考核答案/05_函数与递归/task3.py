import math
 
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True
 
s = input().strip()
# 构造回文数：去掉最后一位，反转后拼到末尾
pal = int(s + s[:-1][::-1])
print("prime" if is_prime(pal) else "noprime")