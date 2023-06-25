class phan_so:
    def __init__(self, a, b):
        self.tu_so = a
        self.mau_so = b
    def __add__(self, other):
        tu_so = self.tu_so * other.mau_so + self.mau_so * other.tu_so
        mau_so = self.mau_so * other.mau_so
        return str(tu_so) + "/" + str(mau_so)

ps1 = phan_so(1, 2)
ps2 = phan_so(3, 4)
print("Ket qua cua phep cong hai phan so la :", ps1 + ps2)