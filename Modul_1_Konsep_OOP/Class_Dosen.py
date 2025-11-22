class Dosen :
    def __init__(self, nama, nidn):
        self.nama = nama
        self.nidn = nidn
    
    #method
    def ajar_mata_kuliah(self, mata_kuliah):
        return f"Halo, Saya {self.nama}, dengan NiDN {self.nidn}, saya mengajar mata kuliah {mata_kuliah}"
    
#Pembuatan object
dosen1 = Dosen ("HyuzaNuzumi", "202412004")
dosen2 = Dosen ("HyuzaNozomi", "202412002")

print(dosen1.ajar_mata_kuliah("Pemrograman Berorientasi Objek"))
print(dosen2.ajar_mata_kuliah("Pemrograman Object Oriented Programming"))