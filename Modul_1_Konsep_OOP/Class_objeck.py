class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def tampilkan_info(self):
        return f"Halo, Saya {self.nama}, dengan NIM {self.nim}" 


#Pembuatan object
mhs1 = Mahasiswa("HyuzaNuzumi", "TI202412004")  
msh2 = Mahasiswa("NuzumiHyuza", "TI202412002")

print(mhs1.perkenalan())
print(msh2.perkenalan())