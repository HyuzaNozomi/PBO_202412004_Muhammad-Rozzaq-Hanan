class UmurExpectationError(Exception):
    """Kesalahan umum yang digunakan."""
    pass

class UmurTerlaluMudaError(Exception):
    """Custom exception untuk umur kurang dari 5 tahun."""
    pass

class UmurTerlaluTuaError(Exception):
    """Custom exception untuk umur lebih dari 100 tahun."""
    pass

class AkunTidakDiizinkanError(Exception):
    """Custom exception untuk akun yang tidak diizinkan (umur < 18)."""
    pass

def set_umur(umur):
    if umur < 0:
        raise UmurExpectationError("Umur tidak boleh negatif.")
    elif umur < 5:
        raise UmurTerlaluMudaError("Umur terlalu muda. Minimal umur 5 tahun.")
    elif umur > 100:
        raise UmurTerlaluTuaError("Umur terlalu tua. Maksimal umur 100 tahun.")
    elif umur > 150:
        raise UmurExpectationError("Umur terlalu besar periksa kembali inputan anda.")
    return umur

def daftar_akun(umur):
    """Fungsi untuk mendaftar akun. Hanya menerima umur 18 ke atas."""
    if umur < 18:
        raise AkunTidakDiizinkanError("Anda harus berusia minimal 18 tahun untuk mendaftar akun.")
    return f"Akun berhasil dibuat untuk umur {umur} tahun."
  
if __name__ == "__main__":
    umur_valid = None
    
    # Loop untuk input umur sampai valid
    while True:
        try:
            umur = int(input("Masukkan umur Anda: "))
            umur_valid = set_umur(umur)
            break  # Keluar dari loop jika input valid
        except ValueError:
            print("Input harus berupa bilangan bulat. Silakan coba lagi.\n")
        except UmurTerlaluMudaError as utme:
            print(f"Error: {utme}. Silakan coba lagi.\n")
        except UmurTerlaluTuaError as utte:
            print(f"Error: {utte}. Silakan coba lagi.\n")
        except UmurExpectationError as uee:
            print(f"Error: {uee}. Silakan coba lagi.\n")
    
    print(f"Umur berhasil disimpan: {umur_valid} tahun\n")
    
    # Fungsi daftar akun
    try:
        hasil_daftar = daftar_akun(umur_valid)
        print(hasil_daftar)
    except AkunTidakDiizinkanError as adi:
        print(f"Pendaftaran gagal: {adi}")