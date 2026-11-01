import sys
 
def main():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1
    A = [int(data[idx + i]) for i in range(n)]; idx += n
    B = [int(data[idx + i]) for i in range(n)]; idx += n
 
    # 先全部晚上吃
    total = sum(B)
    # 计算每个巧克力改成早上吃的增益
    diff = [A[i] - B[i] for i in range(n)]
    diff.sort(reverse=True)
    # 选增益最大的 k 个
    total += sum(diff[:k])
 
    print(total)
 
main()