# Khai bao lop Nhan Vien
class NhanVien:
    # Phuong thuc khoi tao
    def __init__(self, maNV, tenNV, luong, sanluong):
        self.maNV = maNV
        self.tenNV = tenNV
        self.luong = luong
        self.sanluong = sanluong
    # Phuong thuc xuat thong tin nhan vien
    def xuat(self):
        print("Ma nhan vien : ", self.maNV)
        print("Ten nhan vien : ", self.tenNV)
        print("Luong : ", self.luong)
    # Phuong thuc tinh thuong cho nhan vien dua tren san luong
    def tinhThuong(self, thuong):
        if self.sanluong > 200:
            self.luong = thuong + 200000
        elif self.sanluong <= 200 and self.sanluong > 100:
            self.luong = thuong + 100000


dsNhanVien = []
n = int(input("Nhap vao so luong nhan vien : "))
for i in range(n):
    maNV = input("Nhap vao ma nhan vien : ")
    tenNV = input("Nhap vao ten nhan vien : ")
    luong = int(input("Nhap vao luong cua nhan vien : "))
    sanluong = int(input("Nhap vao san luong cua nhan vien : "))
    dsNhanVien.append(NhanVien(maNV, tenNV, luong, sanluong))

print('\nTien luong cua nhan vien truoc khi nhan thuong la : ')

for i in range(len(dsNhanVien)):
    print("Nhan vien thu", i + 1, ": ")
    dsNhanVien[i].xuat()

print('\nTien luong cua nhan vien sau khi nhan thuong : ')
for i in range(len(dsNhanVien)):
    print("Nhan vien thu", i + 1, ": ")
    dsNhanVien[i].tinhThuong(dsNhanVien[i].luong)
    dsNhanVien[i].xuat()