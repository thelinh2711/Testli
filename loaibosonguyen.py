def check(n):
    for i in n:
        if not i.isdigit():
            return True
    if int(n)<2147483648 and int(n)>-2147583648:
        return False
    return True
file = open('b.txt', 'r')
a = []
for line in file:
    for i in line.split():
        if check(i)==True:
            a.append(i)
a.sort()
for i in a:
    print(i, end=" ")