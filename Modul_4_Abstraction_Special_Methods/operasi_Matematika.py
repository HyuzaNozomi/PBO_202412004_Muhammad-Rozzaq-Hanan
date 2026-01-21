def operasi():
    print("==== Operasi Matematika Aman ====")
    print("Pilih Operasi:")
    print("A.Pembagian")
    print("B.Perkalian")

    pilihan = input("Masukkan Piilihan (A/B): ").strip()

    x = input("Masukkan angka pertama: ").strip()
    y = input("Masukkan angka kedua: ").strip()

    try:
        # validasi input tidak boleh kosong
        if x == "" or y == "":
            raise ValueError("Input tidak boleh kosong.")

        a = float(x)
        b = float(y)

        # validasi bilangan harus posisitif
        if a < 0 or b < 0:
            raise ValueError("Hanya menerima bilangan positif.")

        if pilihan == "A":
            # Pembagian
            # dapat memunculkan ZeroDivisionError
            hasil = a / b
        elif pilihan == "B":
            # Perkalian
            hasil = a * b
        else:
            raise ValueError("Pilihan operasi tidak valid. Pilih A atau B.")
    
    except ValueError as ve:
        print(f"Error: {ve}")

    except ZeroDivisionError:
        print("Error: Pembagian dengan nol tidak diperbolehkan.")

    except Exception as e:
        print(f"Terjadi kesalahan tak terduga: {e}")

    else:
        # hanya berjalan jika tidak ada error
        print(f"Hasil operasi: {hasil}")
    
    finally:
        print("Terima kasih telah menggunakan program operasi matematika.")

if __name__ == "__main__":
    operasi()