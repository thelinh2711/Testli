a, k, n=[int(x) for x in input().split()]
b = k - a%k
ok = 0
for i in range(b, n-a+1, k):
    print(i, end=" ")
    ok = 1
if ok == 0:
    print("-1", end=" ")
