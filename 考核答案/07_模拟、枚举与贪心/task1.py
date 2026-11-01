import sys
 
def main():
    data = sys.stdin.read().split()
    n, t = int(data[0]), int(data[1])
    arr = list(data[2])
    dot = arr.index('.')
 
    # 找小数点后第一个 >= '5' 的位置
    i = next((p for p in range(dot + 1, len(arr)) if arr[p] >= '5'), -1)
 
    while i > dot and t > 0:
        t -= 1
        arr = arr[:i]                    # 舍掉 i 及之后
        i -= 1
        if i == dot:                     # 进位到整数部分
            j, carry = dot - 1, 1
            while j >= 0 and carry:
                v = int(arr[j]) + 1
                arr[j] = '0' if v == 10 else str(v)
                carry = v == 10
                j -= 1
            if carry:
                arr.insert(0, '1')
                dot += 1
            arr = arr[:dot]
            break
        arr[i] = str(int(arr[i]) + 1)    # 前一位 +1
        if arr[i] < '5':
            break
 
    s = "".join(arr)
    if '.' in s:
        s = s.rstrip('0').rstrip('.')
    print(s)
 
main()