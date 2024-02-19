import math
def snt(n):
    if n<2: return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n%i==0:
            return False
    return True
def sodao(n):
    x = 0
    while n > 0:
        x = x * 10 + n % 10
        n = n // 10
    return x
def tongchuso(n):
    x = 0
    while n > 0:
        x += n%10
        n = n//10
    return x
def ktra(n):
    if snt(n)==False: return False
    if snt(sodao(n))==False: return False
    if snt(tongchuso(n))==False: return False
    while n > 0:
        x = n%10
        if snt(x)==False: return False
        n = n//10
    return True
t = int(input())
for i in range(t):
    n=int(input())
    if ktra(n)==True:
        print("Yes")
    else: print("No")