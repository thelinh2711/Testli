p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    a = input()
    if a == "0":
        break
    n, s = a.split()
    k = int(n)
    ans = ""
    for i in s:
        for j in range(28):
            if i == p[j]:
                ans = p[(j+k)%28] + ans
    print(ans)


