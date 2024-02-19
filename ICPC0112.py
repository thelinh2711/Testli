import math
def snt(n):
    if n<2: return False
    for i in range(2, int(math.sqrt(n)+1), 1):
        if n % i == 0: return False
    return True
t = int(input())
for i in range(t):
    n = int(input())
    dem = 0
    for i in range(5, n, 2):
        if snt(i)==True and snt(i+2)==True and snt(i+6)==True:
            if i+6<n: dem += 1
        if snt(i)==True and snt(i+4)==True and snt(i+6)==True:
            if i+6<n: dem += 1
    print(dem)