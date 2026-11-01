import sys
 
def solve(cnt):
    odd = [d for d in range(10) if cnt[d] % 2 == 1]
    if len(odd) > 1:
        return "-1"
 
    half = []
    for d in range(10):
        half.extend([str(d)] * (cnt[d] // 2))
 
    mid = str(odd[0]) if odd else ""
 
    # 左半边为空
    if not half:
        return mid if mid else "0"
 
    # 左半边首位是 0，需要把最小的非零数码换到最前
    if half[0] == '0':
        for d in range(1, 10):
            if cnt[d] >= 2:
                # 找到最小的可用非零数码 d
                # 从 half 中移除一个 d，放到最前面
                half.remove(str(d))
                half.insert(0, str(d))
                break
        else:
            # 没有任何非零数码可用，左半边只能全是 0
            if mid and mid != '0':
                return mid
            return "0"
 
    s = "".join(half)
    return s + mid + s[::-1]
 
def main():
    data = sys.stdin.read().split()
    if not data:
        return
    line = data[0] if len(data) == 1 else "".join(data)
    print(solve([int(c) for c in line]))
 
main()