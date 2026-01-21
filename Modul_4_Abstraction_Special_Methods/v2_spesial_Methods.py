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

    def __len__(self):
        return len(self.nama)

    def __eq__(self, other):
        return self.nilai == other.nilai

# Contoh penggunaan
a = Mahasiswa("Nan", 99)
b = Mahasiswa("Han", 95)
c = Mahasiswa("Ali", 99)

print("=== Representasi String ===")
print(a)
print(b)
print(c)

print("\n=== Perbandingan Kesetaraan Nilai ===")
print(f"{a.nama} == {b.nama}: {a == b}")
print(f"{a.nama} == {c.nama}: {a == c}")

print("\n=== Panjang Nama (len) ===")
print(f"Panjang nama {a.nama}: {len(a)}")
print(f"Panjang nama {b.nama}: {len(b)}")

print("\n=== Operasi Matematika ===")
print(f"Total nilai ({a.nama} + {b.nama}): {a + b}")
print(f"Nilai {a.nama} x 2: {a * 2}")

print("\n=== Perbandingan Nilai ===")
if b > a:
    print(f"{b.nama} memiliki nilai lebih besar dari {a.nama}")
else:
    print(f"{a.nama} memiliki nilai lebih besar dari atau sama dengan {b.nama}")

print("\n=== Pengurutan Mahasiswa ===")
list_mahasiswa = [a, b, c]
print("Sebelum diurutkan:")
for m in list_mahasiswa:
    print(f"  {m.nama}: {m.nilai}")

list_terurut = sorted(list_mahasiswa, key=lambda x: x.nilai)
print("Setelah diurutkan (ascending):")
for m in list_terurut:
    print(f"  {m.nama}: {m.nilai}")