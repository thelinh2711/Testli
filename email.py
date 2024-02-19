file = open('CONTACT.in', 'r')
s = set()
for x in file:
    if x[-1] == '\n':
        x = x[:-1]
    if len(x)>0:
        s.add(x.lower())
s = sorted(s)
for i in s:
    print(i)
