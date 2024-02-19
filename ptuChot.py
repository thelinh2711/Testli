for t in range(int(input())):
    n = int(input())
    if n==1:
        x = input()
        print(1)
        continue
    a = [int(x) for x in input().split()]
    maxtrai = [0]*n
    minphai = [0]*n
    maxtrai[0] = a[0]
    for i in range(1, n):
        if a[i]>=maxtrai[i-1]:
            maxtrai[i]=a[i]
        else:
            maxtrai[i] = maxtrai[i-1]
    minphai[n-1] = a[n-1]
    for i in range(n-2, -1, -1):
        if a[i]<=minphai[i+1]:
            minphai[i]= a[i]
        else:
            minphai[i] = minphai[i+1]
    cnt = 0
    if a[0]<minphai[1]:
        cnt += 1
    if a[n-1]>=maxtrai[n-2]:
        cnt += 1
    for i in range(1, n-1):
        if a[i]>=maxtrai[i-1] and a[i]<minphai[i+1]:
            cnt += 1
    print(cnt)