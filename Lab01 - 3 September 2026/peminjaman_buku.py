# =====================================================================
# Nama  : Vicky Ibrahimovic
# NPM   : 2606888572
# Kelas : D
# =====================================================================
# Perbaiki error yang muncul dan kerjakan setiap TODO di bawah.
# =====================================================================

print("======================================== ")
print("        WELCOME TO PACIL LIBRARY ")
print("======================================== ")

# --- Bagian input ------------------------------------------------------
judul_buku = input("Masukkan judul buku: ")
jumlah_buku = int(input("Masukkan jumlah buku yang ingin dipinjam: "))
harga_sewa = int(input("Masukkan harga sewa per buku (rupiah): "))
# TODO 1: Tambahkan beberapa input dan simpan hasilnya ke dalam variabel
#         diskon, nama_bank, saldo_awal, dan durasi_peminjaman. Gunakan
#         tipe data yang sesuai untuk setiap input, seperti yang diminta
#         pada spesifikasi program.

# Input user berupa diskon dan dikonversi ke tipe data float
diskon = float(input("Masukkan diskon (%): "))

# Input user berupa nama_bank
nama_bank = input("Masukkan nama bank pembayaran: ")

# Input user berupa saldo_awal dan dikonversi ke tipe data integer
saldo_awal = int(input("Masukkan saldo awal (rupiah): "))

# Input user berupa durasi_peminjaman dan dikonversi ke tipe data integer
durasi_peminjaman = int(input("Masukkan durasi peminjaman (hari): "))

# --- Bagian proses -------------------------------------------------------
# TODO 2: Konversi durasi_peminjaman (dalam hari) menjadi minggu dan hari.
#         Simpan jumlah minggu ke variabel minggu, dan sisa hari ke
#         variabel hari.
# Keterangan: manfaatkan operator pembagian bulat (//) untuk mendapatkan
#             jumlah minggu, dan operator modulo (%) untuk mendapatkan
#             sisa hari.

# Menghitung Minggu berdasarkan durasi peminjaman dibagi 7 menggunakan operator pembagian pembulatan 
minggu = durasi_peminjaman // 7

# Menghitung hari berdasarkan durasi peminjaman modulo 7 menggunakan operator modulo
hari = durasi_peminjaman % 7


# TODO 3: Bentuk variabel kode_peminjaman dengan menggabungkan judul_buku,
#         jumlah_buku, dan nama_bank.

# Membuat kode peminjaman dengan menggabungkan judul_buku, jumlah_buku, dan nama_bank dengan terlebih dahulu konversi jumlah buku ke string 
kode_peminjaman = judul_buku + str(jumlah_buku)+ nama_bank

# Menghitung subtotal dengan harga_sewa dan jumlah_buku menggunakan operator perkalian dan dikonversi ke float
subtotal = float(harga_sewa * jumlah_buku)

# TODO 4: Hitung nominal_diskon, yaitu persentase diskon dikali subtotal,
#         lalu dibagi 100. Simpan ke variabel nominal_diskon.
# Menghitung nominal diskon dengan diskon dan subtotal menggunakan operator perkalian lalu dibagi 100 menggunakan operator pembagian
nominal_diskon = diskon * subtotal /100

# TODO 5: Hitung total_bayar, yaitu subtotal dikurangi nominal_diskon.
#         Simpan ke variabel total_bayar.

# Menghitung total_bayar dengan subtotal dan nominal diskon menggunakan operator pengurangan
total_bayar = subtotal - nominal_diskon

# Menghitung sisa_saldo dengan saldo_awal dan total_bayar menggunakan operator pengurangan
sisa_saldo = saldo_awal - total_bayar


# --- Bagian output ---------------------------------------------------
print("======================================== ")
print("              RENTAL SUMMARY ")
print("======================================== ")
print("----------- DETAIL PEMINJAMAN ----------- ")
print("Buku : " + judul_buku)
print("Durasi Peminjaman : " + str(minggu) + " minggu " + str(hari) + " hari")
print("Kode Peminjaman : " + kode_peminjaman)
print("----------- DETAIL PEMBAYARAN ----------- ")
# TODO 6: Tampilkan subtotal, nominal diskon, total pembayaran, dan sisa saldo
#         menggunakan format output yang sesuai dengan contoh pada spesifikasi
#         program.
# Menampilkan Subtotal
print(f"Subtotal : Rp{subtotal}")
# Menampilkan Diskon dan nominal Diskon
print(f"Diskon ({int(diskon)}%) : Rp{nominal_diskon}")
# Menampilkan Total Pembayaran
print(f"Total Pembayaran : Rp{total_bayar}")
# Menampilkan Sisa saldo dan nama bank
print(f"Sisa Saldo {nama_bank} Anda : Rp{sisa_saldo}")
print("======================================== ")