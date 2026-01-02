from abc import ABC, abstractmethod
import math

# Class Bentuk
class Bentuk(ABC):
    @abstractmethod
    def luas(self):
        pass

    @abstractmethod
    def keliling(self):
        pass

# Class Lingkaran
class Lingkaran(Bentuk):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def Luas(self):
        return math.pi * (self.jari_jari ** 2)
    
    def Keliling(self):
        return 2 * math.pi * self.jari_jari

# Class Persegi
class Persegi_Panjang(Bentuk):
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def Luas(self):
        return self.panjang * self.lebar

    def Kelliling(self):
        return 2 * (self.panjang + self.Lebar)

# Contoh penggunaan
l = Lingkaran(5)
p = Persegi_Panjang(4, 3)

print(f"Luas Lingkaran: {l.luas():.2f}")
print(f"Keliling Lingkaran: {l.keliling():.2f}")
print(f"Luas Persegi Panjang: {p.luas():.2f}")
print(f"Keliling Persegi Panjang: {p.keliling():.2f}")