for t in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    dem = 0
    for i in range(n-1):
        m = min(a[i], a[i+1])
        M = max(a[i], a[i+1])
        while m*2<M:
            dem += 1
            m *= 2
    print(dem)