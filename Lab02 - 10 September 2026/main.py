# Print Header
print(
"""=====================================
        SISTEM PENGIRIMAN PAKET
=====================================""")

# Input Jenis layanan
jenis_layanan = input("Masukkan jenis layanan (reguler/express/same_day): ")

# Validasi Input Jenis Layanan
if jenis_layanan not in ("reguler","express","same_day"):
    print("""
=====================================
Jenis layanan tidak dikenali.
=====================================
    """)
    exit()

# Input Berat Paket
berat_paket = int(input("Masukkan berat paket (kg): "))

# Input Pecah Belah
pecah_belah = input("Apakah paket pecah belah? (ya/tidak): ")

# Validasi Input Pecah Belah
if pecah_belah not in ("ya","tidak"):
    print("""
=====================================
Input pecah_belah tidak dikenali.
=====================================
    """)
    exit()

# Input Keanggotaan
anggota = input("Apakah pelanggan merupakan anggota? (ya/tidak): ")
# Validasi Input Keanggotaan
if anggota not in ("ya","tidak"):
    print("""
=====================================
Input anggota tidak dikenali.
=====================================
    """)
    exit()
    
# Input Metode Pembayaran
metode_pembayaran = input("Masukkan metode pembayaran (tunai/saldo): ")
# Validasi Input Metode Pembayaran
if metode_pembayaran not in ("tunai","saldo"):
    print("""
=====================================
Input metode_pembayaran tidak dikenali.
=====================================
    """)
    exit()



# Percabangan untuk Mementukan biaya dasar dari tarif masing masing jenis layanan
if jenis_layanan=="reguler":
    biaya_dasar = berat_paket * 4000 #Layanan Reguler
elif jenis_layanan=="express":
    biaya_dasar = berat_paket * 7000 #Layanan Express
elif jenis_layanan=="same_day":
    biaya_dasar = berat_paket * 10000 #Layanan Same Day

# Percabangan untuk Mementukan biaya penanganan dari input pecah belah
if pecah_belah=="ya":
    biaya_penanganan = 8000 
elif pecah_belah=="tidak":
    biaya_penanganan = 0

# Percabangan untuk Mementukan diskon dari input anggota
if anggota=="ya":
    diskon = biaya_dasar*20/100
    # Percabangan untuk membuat maksimal diskon menjadi 15000
    if diskon > 15000:
        diskon = 15000
elif anggota=="tidak":
    diskon = 0

# Perhitungan Total Biaya
total_biaya = biaya_dasar - diskon + biaya_penanganan

# Percabangan untuk menentukan input saldo jika metode pembayaran adalah saldo
if metode_pembayaran == "saldo":
    saldo = int(input("Masukkan saldo: "))
        

# Print Rincian pengiriman
print("\n\n========== RINCIAN PENGIRIMAN ==========")
# Print Biaya Dasar
print(f"Biaya dasar         : Rp {biaya_dasar}")
# Print Diskon anggota yang dikonversi ke integer
print(f"Diskon anggota      : Rp {int(diskon)}")
# Print Biaya Penanganan
print(f"Biaya penanganan    : Rp {biaya_penanganan}")
print("-----------------------------------------")
# Print Total Biaya yang dikonversi ke integer
print(f"Total biaya         : Rp {int(total_biaya)}")
# Percabangan untuk print informasi selanjutnya menggunakan kondisi dari metode pembayaran
if metode_pembayaran == "saldo":
    # Percabangan jika saldo tidak mencukupi dan sebaliknya
    if saldo < total_biaya:
        print("Saldo tidak mencukupi")
        print(f"Kekurangan saldo    : Rp {int(total_biaya-saldo)}")
    else:
        print(f"Sisa Saldo          : Rp {int(saldo-total_biaya)}")
# Pengecualian jika menggunakan metode pembayaran tunai
elif metode_pembayaran == "tunai":
    print("Pembayaran dilakukan secara tunai.")
print("=========================================")