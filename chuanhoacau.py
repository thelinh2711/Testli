m = []
while(True):
    try:
        m.append(input())
    except:
        break
for o in m:
    s = o.split()
    ok, cnt = 0, 0
    k = len(s)
    for i in s:
        check = 1
        cnt += 1
        a = list(i)
        if ok == 0:
            print(a[0].upper(), end="")
            for j in range(1, len(a)):
                print(a[j].lower(), end="")
            ok = 1
        else:
            print(i.lower(), end="")
        if (s[k-1]=="." or s[k-1]=="?" or s[k-1]=="!") and cnt == k-1:
            print(s[k-1], end="")
            check = 0
            break
        if cnt != k:
            print(" ", end="")
    if a[len(a)-1]!= "." and a[len(a)-1]!="!" and a[len(a)-1]!="?" and check!=0:
        print(".")
    else:
        print()