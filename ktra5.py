class phim:
    def __init__(self,ma, theloai, ngay, ten, tap):
        self.ma = 'P{:03d}'.format(ma)
        self.ngay = ngay
        self.ten = ten
        self.tap = tap
        self.theloai = theloai
    def getNgay(self):
        x = ''
        x = x+self.ngay[6::]+self.ngay[3:5]+self.ngay[0:2]
        return int(x)

n, m = [int(x) for x in input().split()]
t = []
for i in range(n):
    t.append(input())
a = []
for i in range(m):
    s = input()
    a.append(phim(i+1, t[int(s[2:])-1], input(), input(), int(input())))
a = sorted(a, key=lambda x : (x.getNgay(), x.ten, -x.tap))
for i in a:
    print(i.ma, end=" ")
    print(i.theloai, end=" ")
    print(i.ngay, end=" ")
    print(i.ten, end=" ")
    print(i.tap)
