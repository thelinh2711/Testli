s = "0123456789ABCDEF"
t = int(input())
for k in range(t):
    b = int(input())
    n = int(input(), 2)
    ans = ""
    while n>0:
        x = n%b
        ans = s[x] + ans
        n = n//b
    print(ans)

