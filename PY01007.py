import math
t = int(input())
for i in range(t):
    n, x, m = [float(j) for j in input().split()]
    x = x / 100
    k = math.log(m/n, 1+x)
    if k == int(k): print(k)
    else: print(int(k)+1)