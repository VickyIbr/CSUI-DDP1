# Deklarasi Daftar Huruf Vokal Menggunakan Python
huruf_vokal = ("A","I","U","E","O")

# Input nama beserta penggunaan method replace untuk menghapus karakter spasi
nama = input("Masukkan nama Asdos: ").replace(" ","")

# Deklarasi String Kosong untuk Kode Asdos
kode_asdos = ""

# Memulai Perulangan berdasarkan Input Nama
for n in nama:
    # Percabangan Jika huruf bukan vokal maka akan di append ke string kode_asdos
    if n not in huruf_vokal:
        kode_asdos += n
    # Percabangan Jika Jumlah Kode asdos adalah 4 huruf maka akan mengakhiri peulangan dengan break
    if len(kode_asdos) == 4:
        break

# Print Kode Asdos
print(f"Kode Asdos: {kode_asdos}")
