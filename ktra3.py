for t in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    dem = 0
    for i in range(1, n):
        x = max(a[i-1], a[i])
        y = 2*min(a[i-1], a[i])
        while x>y:
            dem += 1
            y = y*2
    print(dem)