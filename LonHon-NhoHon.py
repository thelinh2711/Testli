from sys import setrecursionlimit
arr, names = [], set()
n = int(input())
for i in range(n):
    name1, sign, name2 = input().split()
    names.add(name1)
    names.add(name2)
    if sign == '>':
        arr.append((name1, name2))
    else:
        arr.append((name2, name1))
a = sorted(names)
N = len(a)
def ind(name):
    l, r = 0, N
    while l<r:
        mid = (l+r)>>1
        if a[mid] == name:
            return mid
        if a[mid]<name:
            l = mid+1
        else: r = mid
    return -1

ke = [[] for i in range(N)]
for n1, n2 in arr:
    ke[ind(n1)].append(ind(n2))
vs = [0]*N
setrecursionlimit(10**6)
def dfs(i):
    vs[i]=1
    for j in ke[i]:
        if vs[j]==0:
            if(dfs(j)):
                return True
        if vs[j]==1: return True
    vs[i]=2
    return False

ok = False
for i in range(N):
    if vs[i] == 0:
        if(dfs(i)):
            ok = True
            break

if ok:
    print("impossible")
else:
    print("possible")