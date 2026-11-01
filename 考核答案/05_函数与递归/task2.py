import sys
 
def days_of_month(y, m):
    if m == 2:
        if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
            return 29
        return 28
    if m in (4, 6, 9, 11):
        return 30
    return 31
 
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    y, m, x = map(int, line.split())
    days = days_of_month(y, m)
 
    # 年 - 月 部分（月补零 2 位）
    ym = f"{y:04d}-{m:02d}"
    cnt = ym.count(str(x)) * days
 
    # 枚举日
    for d in range(1, days + 1):
        cnt += f"{d:02d}".count(str(x))
 
    print(cnt)