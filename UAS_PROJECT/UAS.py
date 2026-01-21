import tkinter as tk
from tkinter import ttk, messagebox
from abc import ABC, abstractmethod

#Custom Exception 
class HargaTidakValidError(Exception):
    """Error custom jika harga yang diinput negatif atau nol."""
    def __init__(self, message="Harga tidak boleh negatif atau nol"):
        self.message = message
        super().__init__(self.message)

#Abstraction & Encapsulation
class Produk(ABC):
    def __init__(self, nama, harga, stok):
        self.nama = nama              # Public
        self._stok = stok             # Protected (_attribute)
        self.__harga = harga          # Private (__attribute)

    # Getter untuk private attribute
    @property
    def harga(self):
        return self.__harga

    # Setter untuk private attribute (Validasi data)
    @harga.setter
    def harga(self, nilai):
        if nilai <= 0:
            raise HargaTidakValidError()
        self.__harga = nilai

    # Abstract method (Syarat: @abstractmethod)
    @abstractmethod
    def hitung_estimasi_jual(self):
        pass

    # Special Method (Syarat: __str__)
    def __str__(self):
        return f"{self.nama} | Stok: {self._stok}"

#Inheritance & Polymorphism 
class Laptop(Produk):
    def __init__(self, nama, harga, stok, processor):
        super().__init__(nama, harga, stok)
        self.processor = processor # Atribut spesifik

    # Polymorphism: Implementasi metode abstrak
    def hitung_estimasi_jual(self):
        # Laptop ada pajak barang mewah 10%
        return self.harga * 1.1

    def __str__(self):
        return f"[Laptop] {super().__str__()} | Proc: {self.processor}"

class Smartphone(Produk):
    def __init__(self, nama, harga, stok, kamera):
        super().__init__(nama, harga, stok)
        self.kamera = kamera # Atribut spesifik

    # Polymorphism: Implementasi metode abstrak dengan perilaku beda
    def hitung_estimasi_jual(self):
        # Smartphone pajak standar 5%
        return self.harga * 1.05

    def __str__(self):
        return f"[HP] {super().__str__()} | Cam: {self.kamera}MP"

#Relasi & Collections
class ManajemenGudang:
    """Kelas untuk mengelola koleksi object (Aggregation)."""
    def __init__(self):
        self.daftar_produk = [] # Data: Collection (List) menyimpan object

    def tambah_produk(self, produk):
        self.daftar_produk.append(produk)

    def ambil_semua_data(self):
        return self.daftar_produk

#GUI Implementation
class AplikasiTokoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Manajemen Stok Elektronik")
        self.root.geometry("600x500")

        # Association: GUI terhubung dengan logic inventory
        self.gudang = ManajemenGudang()

        self.setup_ui()

    def setup_ui(self):
        # Frame Input
        frame_input = tk.LabelFrame(self.root, text="Input Data Produk")
        frame_input.pack(padx=10, pady=10, fill="x")

        # -- Form Inputs --
        tk.Label(frame_input, text="Nama Produk:").grid(row=0, column=0, sticky="w")
        self.entry_nama = tk.Entry(frame_input)
        self.entry_nama.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_input, text="Harga (Rp):").grid(row=1, column=0, sticky="w")
        self.entry_harga = tk.Entry(frame_input)
        self.entry_harga.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame_input, text="Stok:").grid(row=2, column=0, sticky="w")
        self.entry_stok = tk.Entry(frame_input)
        self.entry_stok.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(frame_input, text="Jenis:").grid(row=3, column=0, sticky="w")
        self.combo_jenis = ttk.Combobox(frame_input, values=["Laptop", "Smartphone"])
        self.combo_jenis.current(0)
        self.combo_jenis.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(frame_input, text="Info Khusus (Proc/Cam):").grid(row=4, column=0, sticky="w")
        self.entry_spek = tk.Entry(frame_input)
        self.entry_spek.grid(row=4, column=1, padx=5, pady=5)

        # -- Button Aksi --
        btn_simpan = tk.Button(frame_input, text="Simpan Data", command=self.aksi_simpan, bg="#4CAF50", fg="white")
        btn_simpan.grid(row=5, column=1, pady=10, sticky="e")

        # Frame Output
        frame_output = tk.LabelFrame(self.root, text="Daftar Stok (Memory)")
        frame_output.pack(padx=10, pady=10, fill="both", expand=True)

        self.text_area = tk.Text(frame_output, height=10)
        self.text_area.pack(padx=5, pady=5, fill="both", expand=True)

    #Exception Handling
    def aksi_simpan(self):
        try:
            # Mengambil data dari GUI
            nama = self.entry_nama.get()
            harga_raw = self.entry_harga.get()
            stok_raw = self.entry_stok.get()
            jenis = self.combo_jenis.get()
            spek = self.entry_spek.get()

            # Validasi input dasar
            if not nama or not harga_raw or not stok_raw:
                raise ValueError("Semua field harus diisi!")

            harga = float(harga_raw)
            stok = int(stok_raw)

            # Polimorfisme dalam pembuatan objek
            produk_baru = None
            if jenis == "Laptop":
                produk_baru = Laptop(nama, harga, stok, spek)
            else:
                produk_baru = Smartphone(nama, harga, stok, spek) # spek disini adalah kamera

            # Simpan ke collection
            self.gudang.tambah_produk(produk_baru)

        except ValueError as ve:
            # Menangani error konversi tipe data atau field kosong
            messagebox.showerror("Input Error", f"Data tidak valid: {ve}")
        except HargaTidakValidError as he:
            # Menangani custom exception dari Setter
            messagebox.showerror("Logic Error", str(he))
        except Exception as e:
            # Catch-all error
            messagebox.showerror("Error", f"Terjadi kesalahan: {e}")
        else:
            # Dijalankan jika TIDAK ada error
            messagebox.showinfo("Sukses", f"Berhasil menyimpan {nama}!")
            self.update_tampilan()
        finally:
            # Dijalankan bagaimanapun kondisinya (untuk reset form atau logging)
            print("Percobaan input data selesai.")
            # Opsional: self.entry_nama.delete(0, tk.END)

    def update_tampilan(self):
        self.text_area.delete(1.0, tk.END)
        data = self.gudang.ambil_semua_data()
        
        for idx, item in enumerate(data):
            # Menggunakan method polimorfisme hitung_estimasi_jual
            estimasi = item.hitung_estimasi_jual()
            
            # Menggunakan __str__
            teks = f"{idx+1}. {item} | Harga Dasar: {item.harga} | Est. Jual (+Pajak): {estimasi:.0f}\n"
            self.text_area.insert(tk.END, teks)

#Main Loop
if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiTokoGUI(root)
    root.mainloop()