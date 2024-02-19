t = int(input())
for k in range(t):
    s = input()
    x, y = 0, 0
    s = s + "linh"
    for i in range(len(s)):
        if s[i]>='0' and s[i]<='9':
            y = y*10 + int(s[i])
        else:
            if y!=0:
                x = max(x, y)
                y = 0

    print(x)
