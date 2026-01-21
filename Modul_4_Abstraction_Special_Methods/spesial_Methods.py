# Mahasiswa
class Mahasiswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai

    def __str__(self):
        return f"Nama: {self.nama}, Nilai: {self.nilai}"

    def __gt__(self, other):
        return self.nilai > other.nilai

    def __add__(self, other):
        return self.nilai + other.nilai

    def __mul__(self, faktor):
        return self.nilai * faktor

# Contoh penggunaan
a = Mahasiswa("Nan", 99)
b = Mahasiswa("Han", 95)

print(a)
print(b)

if b > a:
    print(f"{b.nama} memiliki nilai lebih besar dari {a.nama}")

print("Total nilai:", a + b)
print("Nilai Nan x 2 =", a * 2)