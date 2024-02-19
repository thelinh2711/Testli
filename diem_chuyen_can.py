class DiemChuyenCan:
    def __init__(self, maSV, hoTen, lop):
        self.maSV = maSV
        self.hoTen = hoTen
        self.lop = lop
        self.diemCC = 10
        self.ghiChu = ""

    def get_ma(self):
        return self.maSV

    def put_diem_CC(self, s):
        for char in s:
            if char == 'x':
                continue
            elif char == 'v':
                self.diemCC -= 2
            else:
                self.diemCC -= 1
        if self.diemCC <= 0:
            self.diemCC = 0
            self.ghiChu = "KDDK"

    def __str__(self):
        return f"{self.maSV} {self.hoTen} {self.lop} {self.diemCC} {self.ghiChu}"


if __name__ == "__main__":
    t = int(input())
    list_dcc = []
    for _ in range(t):
        ma = input()
        ten = input()
        lop = input()
        list_dcc.append(DiemChuyenCan(ma, ten, lop))

    map_diem_danh = {}
    for _ in range(t):
        ma, diem_danh = input().split()
        map_diem_danh[ma] = diem_danh

    for dcc in list_dcc:
        dcc.put_diem_CC(map_diem_danh[dcc.get_ma()])
        print(dcc)
