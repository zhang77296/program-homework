s = input().strip()
 
cnt = 0
ok = True
for c in s:
    if c == 'a':
        cnt += 1
    else:  # c == 'b'
        cnt -= 1
        if cnt < 0:   # 出现了多余的 b，前面 a 不够配对
            ok = False
            break
 
if ok and cnt == 0:
    print("Good")
else:
    print("Bad")