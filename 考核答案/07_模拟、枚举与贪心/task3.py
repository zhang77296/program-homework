import sys
 
def main():
    s = sys.stdin.read()
    n = len(s)
    res = []
    i = 0
    in_str = False    # 是否在字符串中
    in_cmt = False    # 是否在注释中
 
    while i < n:
        if in_cmt:
            # 找注释结束 */
            if s[i] == '*' and i + 1 < n and s[i + 1] == '/':
                in_cmt = False
                i += 2
            else:
                i += 1
            continue
 
        if in_str:
            # 字符串内：输出所有字符，处理转义和引号
            if s[i] == '\\' and i + 1 < n:
                res.append(s[i])
                res.append(s[i + 1])
                i += 2
                continue
            elif s[i] == '"':
                in_str = False
            res.append(s[i])
            i += 1
        else:
            # 代码区
            if s[i] == '"':
                in_str = True
                res.append(s[i])
                i += 1
            elif s[i] == '/' and i + 1 < n and s[i + 1] == '*':
                in_cmt = True
                i += 2
            else:
                res.append(s[i])
                i += 1
 
    sys.stdout.write("".join(res))
 
main()