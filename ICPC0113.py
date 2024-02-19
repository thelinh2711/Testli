import math
def snt(n):
    if n<2: return False
    for i in range(2, int(math.sqrt(n)+1), 1):
        if n % i == 0: return False
    return True
def sodao(n):
    x = 0
    while n > 0:
        x = x*10 + n%10
        n = n//10
    return x
t = int(input())
for i in range(t):
    n = int(input())
    a = []
    for i in range(13, n, 2):
        if snt(i)==1 and snt(sodao(i))==1:
            if i!=sodao(i) and sodao(i)<n:
                if a.count(i) == 0:
                    a.append(i)
                    a.append(sodao(i))
    for i in a:
        print(i, end=" ")
    print()