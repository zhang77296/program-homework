from functools import cmp_to_key
 
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    nums = data[1:1 + n]  # 直接按字符串处理
 
    # 自定义比较：a 排在 b 前面当且仅当 a+b > b+a
    def cmp(a, b):
        if a + b > b + a:
            return -1
        elif a + b < b + a:
            return 1
        return 0
 
    nums.sort(key=cmp_to_key(cmp))
    print("".join(nums))
 
main()