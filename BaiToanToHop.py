n, k = [int(x) for x in input().split()]
a = {int(x) for x in input().split()}
b = list(a)
b.sort()
c = len(b)
ans = []
key = [0]*(k+1)
def output():
    for i in ans:
        print(i, end=" ")
    print()
def Try(i):
    for j in range(key[i-1]+1, c-k+i+1):
        key[i] = j
        ans.append(b[j-1])
        if i==k:
            output()
        else: Try(i+1)
        ans.pop()
Try(1)