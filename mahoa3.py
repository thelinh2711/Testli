def mahoa(s):
    k, x = 0, ''
    for i in s:
        k += ord(i)-ord('A')
    for i in s:
        x += chr(((ord(i)-ord('A')+k)%26+ord('A')))
    return x
for t in range(int(input())):
    s = input()
    n = len(s)//2
    a = s[0:n]
    b = s[n::]
    a = mahoa(a)
    b = mahoa(b)
    ans = ''
    for i in range(n):
        ans += chr(((ord(a[i])-ord('A')+ord(b[i])-ord('A'))%26 + ord('A')))
    print(ans)