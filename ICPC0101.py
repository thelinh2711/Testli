
n = int(input())
a = [int(x) for x in input().split()]
b = []
for j in a:
    if len(b)==0:
        b.append(j)
    else:
        if (b[-1]+j)%2==0:
            b.pop()
        else:
            b.append(j)
print(len(b))