def check(k):
    for i in a:
        if int(i/k) == int(i/(k+1)):
            return False
    return True
n = int(input())
a = [int(x) for x in input().split()]
s, ans = min(a), 0
for i in range(s, 0, -1):
    if check(i)==True:
        for j in range(n):
            ans += int(a[j]/(i+1))+1
        break
print(ans)