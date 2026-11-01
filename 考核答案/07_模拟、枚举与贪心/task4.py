import sys
 
words = {'zero': '0', 'two': '2', 'four': '4', 'six': '6', 'nine': '9'}
 
def solve(s):
    res = []
    i = 0
    n = len(s)
    while i < n:
        # 优先匹配英文单词（先查更长的）
        matched = False
        for w in ('zero', 'four', 'nine', 'two', 'six'):
            if s.startswith(w, i):
                res.append(words[w])
                i += len(w)
                matched = True
                break
        if matched:
            continue
        # 再匹配单个数字字符
        if s[i] in '02469':
            res.append(s[i])
        i += 1
    return "".join(res)
 
def main():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    out = []
    for k in range(1, t + 1):
        out.append(solve(data[k]))
    print("\n".join(out))
 
main()