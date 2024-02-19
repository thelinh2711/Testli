class Cathi:
    def __init__(self, ma, ngay, time, phong):
        self.ma = 'C{:03d}'.format(ma)
        self.ngay = ngay
        self.time = time
        self.phong = phong
def get_ma(ma):
    return int(ma[1:])
file = open('linh.txt', 'r')
n = int(file.readline().strip())
a = []
for i in range(n):
    ngay = file.readline().strip()
    time = file.readline().strip()
    phong = file.readline().strip()
    a.append(Cathi(i+1, ngay, time, phong))
a.sort(key=lambda cathi:(cathi.ngay, cathi.time, get_ma(cathi.ma)))
for i in a:
    print(i.ma, end=" ")
    print(i.ngay, end=" ")
    print(i.time, end=" ")
    print(i.phong)
file.close()