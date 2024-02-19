for t in range(int(input())):
    n = int(input())
    ds = []
    for i in range(n):
        a, b= [int(x) for x in input().split()]
        ds.append([a, b])
    ds = sorted(ds, key=lambda x:(x[1]))
    dem = 1
    ans = ds[0][1]
    for i in range(1, n):
        if ans <= ds[i][0]:
            dem += 1
            ans = ds[i][1]
    print(dem)