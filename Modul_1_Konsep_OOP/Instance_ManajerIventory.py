class ManajerInventory:
    # inisialisasi inventory sebagai dictionary kosong
    def __init__(self):
        self.inventory = {}

    # menambahkan item ke inventory
    def tambah_item(self, nama_item, jumlah):
        if nama_item in self.inventory:
            # jika item sudah ada, tambahkan jumlahnya
            self.inventory[nama_item] += jumlah 
        else:
            # jika item belum ada, buat entri baru
            self.inventory[nama_item] = jumlah

    # menghapus item dari inventory
    def hapus_item(self, nama_item, jumlah):
        # jika item ad dalam inventory
        if nama_item in self.inventory:
            if self.inventory[nama_item] >= jumlah:
                # kurangi jumlah item
                self.inventory[nama_item] -= jumlah
                # jika jumlah item menjadi 0, hapus item dari inventory
                if self.inventory[nama_item] == 0:
                    del self.inventory[nama_item]
            else:
                print(f"Tidak cukup {nama_item} untuk dihapus.")
        else:
            print(f"{nama_item} tidak ditemukan dalam inventory")
    
    # menampilkan isi inventory
    def tampilkan_inventory(self):
        if not self.inventory:
            print("Inventory kosong")
        else:
            for nama_item, jumlah in self.inventory.items():
                print(f"{nama_item}: {jumlah}")


                