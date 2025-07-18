import math

class PhanSo:
    def __init__(self, tu, mau):
        if mau == 0:
            raise ValueError("Mẫu số không được bằng 0")
        self.tu = tu
        self.mau = mau
        self.rut_gon()

    def rut_gon(self):
        ucln = math.gcd(self.tu, self.mau)
        self.tu //= ucln
        self.mau //= ucln
        if self.mau < 0:  # Đưa dấu âm lên tử số
            self.tu = -self.tu
            self.mau = -self.mau

    def __str__(self):
        return f"{self.tu}/{self.mau}"

    def cong(self, ps_khac):
        tu_moi = self.tu * ps_khac.mau + ps_khac.tu * self.mau
        mau_moi = self.mau * ps_khac.mau
        return PhanSo(tu_moi, mau_moi)

    def tru(self, ps_khac):
        tu_moi = self.tu * ps_khac.mau - ps_khac.tu * self.mau
        mau_moi = self.mau * ps_khac.mau
        return PhanSo(tu_moi, mau_moi)

ps1 = PhanSo(1, 2)
ps2 = PhanSo(1, 3)

tong = ps1.cong(ps2)
hieu = ps1.tru(ps2)

print(f"Tổng: {tong}")  # Kết quả: Tổng: 5/6
print(f"Hiệu: {hieu}")  # Kết quả: Hiệu: 1/6
