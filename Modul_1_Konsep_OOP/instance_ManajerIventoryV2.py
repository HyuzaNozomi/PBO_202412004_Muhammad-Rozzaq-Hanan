class ManajerInventory:
    def __init__(self, Inventory, stock = None):
        self.inventory = Inventory
        self.stock = stock

    def tambah_item(self, nama_item, jumlah):
        # jika item sudah ada, tambahkan jumlahnya
        if nama_item in self.inventory:
            self.inventory[nama_item] += jumlah
        # jika item belum ada, buat entri baru
        else:
            self.inventory[nama_item] = jumlah
        return self.inventory
    
    def hapus_item(self, nama_item, jumlah):
        # jiak item ada dalam inventory
        if nama_item in self.inventory:
            if self.inventory[nama_item] >= jumlah:
                # kurangi jumlah item
                self.inventory[nama_item] -= jumlah
                # jika jumlah item menjadi 0, hapus item dari inventory
                if self.inventory[nama_item] == 0:
                    del self.inventory[nama_item]
            else:
                print(f"Tidak cukup {nama_item} untuk dihapus")
        else: 
            print(f"{nama_item} tidak ditemukan dalam inventory")
        return self.inventory
    
    def tampilkan_inventory(self):
        if not self.inventory:
            print("Inventory kosong")
        else:
            for nama_item, jumlah in self.inventory.items():
                print(f"{nama_item}: {jumlah}")
                return self.inventory
            
# Pengunaan
profesional = ManajerInventory({"BOM": 5, "AK-47": 5, "Medkit": 10})
print(profesional.tampilkan_inventory())

# profesional.tambah_item("BOM", 3)
print(profesional.tambah_item("BOM", 3))

# profesional.hapus_item("AK-47", 2)
print(profesional.hapus_item("AK-47", 2))
    