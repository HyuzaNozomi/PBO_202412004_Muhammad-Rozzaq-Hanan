class kendaraan:
    # class kendaraan / class attribut
    bahan_bakar = "Minyak Nabati"

    # constuctor / instancde method
    def __init__(self, merek, warna, tahun):
        #instance atribut
        self.merek = merek
        self.warna = warna
        self.tahun = tahun

    def info_kendaraan(self):
        return f"kendaraan merek {self.merek}, warna {self.warna}, tahun {self.tahun}"
    
#instansiasi objek
kendaraan1 = kendaraan("Lamborghini", "White", 2024)
kendaraan2 = kendaraan("Ferrari", "Red", 2024)

#Mengakses via class atribut
print(kendaraan.bahan_bakar)

#Mengakses via instance atribut
print(kendaraan1.bahan_bakar)

#Mengubah class atribut
kendaraan.bahan_bakar = "Listrik"

#mengakses via objeck atribut
print(kendaraan1.bahan_bakar)
print(kendaraan2.bahan_bakar)





















#print(kendaraan1.info_kendaraan())
#print(kendaraan2.info_kendaraan())
#print(f"Bahan bakar kendaraan: {kendaraan.bahan_bakar}")


#Instance 
#mengakses data atribut 
#print(kendaraan1.merek)
#print(kendaraan2.merek)
#mengubah data atribut
#kendaraan1.merek = "Bugatti"
#print(kendaraan1.merek)
#print(kendaraan2.merek)