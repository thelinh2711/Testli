t = int(input())
for i in range(t):
    s = input()
    for i in range(0, len(s), 2):
        print(s[i], end="")
        for j in range(int(s[i+1])-1):
            print(s[i], end="")
    print()