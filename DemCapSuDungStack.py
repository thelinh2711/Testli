from sys import stdin
input = stdin.readline
a = []
n = int(input())
for i in range(n):
    a.append(int(input()))

def low(arr, l, x):
    r = len(arr)-1
    while l<r:
        mid = (l+r)>>1
        if arr[mid]<x: l = mid+1
        else:
            r = mid
    return l
z = sorted(set(a))
m = [[] for i in z]
first = [0]*len(z)

for i in range(n):
    a[i] = low(z, 0, a[i])
    m[a[i]].append(i)

def get(arr, start, end, step, root):
    s = []
    for i in range(start, end, step):
        while len(s)>0 and a[s[-1]]<=a[i]:
            s.pop()
        arr[i] = root if len(s)==0 else s[-1]
        s.append(i)
l, r = [0]*n, [0]*n
get(l, 0, n, 1, -1)
get(r, n-1, -1, -1, n)

def dem(arr, start, end):
    if start>=len(arr) or end < arr[start]:
        return 0
    pos = low(arr, start, end)
    if arr[pos]>end:
        pos -= 1
    return pos-start+1
s = 0
for i in range(n):
    if l[i]!=-1:
        s += 1
    if r[i]!=n:
        s += 1
    x = dem(m[a[i]], first[a[i]], r[i]-1)
    s += (x-1)*x//2
    first[a[i]] += x

print(s)
