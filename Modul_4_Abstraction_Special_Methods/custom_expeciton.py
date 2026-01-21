class UmurExpectationError(Exception):
    """Kesalahan umum yang digunakan."""
    pass

def set_umur(umur):
    if umur < 0:
        raise UmurExpectationError("Umur tidak boleh negatif.")
    elif umur > 150:
        raise UmurExpectationError("Umur terlalu besar periksa kembali inputan anda.")
    return umur
  
if __name__ == "__main__":
    try:
        umur = int(input("Masukkan umur Anda: "))
        umur_valid = set_umur(umur)
    except ValueError:
        print("Input harus berupa bilangan bulat.")
    except UmurExpectationError as uee:
        print(uee)
    else:
        print(f"Umur berhasil disimpan: {umur_valid}")