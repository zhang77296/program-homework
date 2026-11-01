import sys
 
def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))
    a.sort()
 
    for i in range(n - 2):
        if a[i] + a[i + 1] > a[i + 2]:
            print(a[i], a[i + 1], a[i + 2])
            return
 
    print("No solution")
 
main()