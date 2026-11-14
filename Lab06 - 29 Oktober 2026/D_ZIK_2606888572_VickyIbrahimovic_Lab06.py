import random #Import random untuk kebutuhan random nama

# Inisialisasi Variabel
anggota = list()
nama_unik = set()
TUGAS = ("Menyapu", "Mengepel", "Merapikan")
petugas = dict()
cadangan = list()

# Print Header
print("""
=== PEMBAGIAN PIKET DEK DEPE ===
1. Tambah anggota
2. Simulasi piket
3. Rekap
4. Selesai""")

# Perulangan Utama untuk pemilihan menu
while True:
    # Input Pilih menu
    pilih = input("Pilih menu: ")

    # Percabangan jika user pilih 1
    if pilih == "1":
        # Input nama untuk anggota
        nama = input("Nama anggota: ").strip().lower()
        # Validasi nama unik agar tidak ada duplicate
        if nama in nama_unik:
            print("Anggota sudah terdaftar")
        else:
            # Menambah anggota ke list dan set anggota dan nama unik
            anggota.append(nama)
            nama_unik.add(nama)
            print(f"Anggota {nama} ditambahkan")

    # Percabangan jika user pilih 2
    elif pilih == "2":
        # Input jumlah petugas
        k = int(input("Jumlah petugas: "))
        # Input Ruang
        ruang = input("Nomor ruang: ")
        # validasi input jumlah petugas untuk sesuai dengan jumlah anggota yang ada
        if k < 1 or k > len(anggota):
            print("Jumlah petugas tidak valid")
            # Melanjutkan ke iterasi setelahnya  jika simulasi tidak valid
            continue
        # Mengkosongkan Dictionary Petugas untuk menghindari overlapping
        petugas.clear()
        # Menyalin Anggota ke cadangan agar list anggota tidak terganggu
        cadangan = anggota.copy()
        # Perulangan untuk assign petugas ke tugasnya
        for i in range(k):
            # Mengambil Angka random menggunakan libary random
            indeks = random.randrange(len(cadangan))
            # Ambil nama random lalu menghapusnya dari list menggunakan angka random sebelumnya
            nama = cadangan.pop(indeks)
            # Assign Petugas dan tugas ke dictionary
            petugas[nama] = TUGAS[i % len(TUGAS)]
        print(f"Hasil simulasi ruang {ruang}")
        # Print Daftar Petugas (menggunakan enumerate agar indeks bisa terbaca)
        for i, (key, value) in enumerate(petugas.items()):
            print(f"{i+1}. {key} -> {value}")

    # Percabangan jika user pilih 3
    elif pilih == "3":
        # Print Toal Anggota unik dan anggotanya
        print(f"Total anggota unik: {len(nama_unik)}")
        print(f"Anggota: {", ".join(nama_unik) if len(nama_unik) >= 1 else "-"} ")
        # Print Hasil semulasi dengan validasi terlebih dahulu
        if len(petugas) >= 1:
            print("Petugas simulasi terakhir.")
            # Print Daftar Petugas (menggunakan enumerate agar indeks bisa terbaca)
            for i, (key, value) in enumerate(petugas.items()):
                print(f"{i+1}. {key} -> {value}")
        else:
            print("Belum ada hasil simulasi")

    # Percabangan jika user pilih 4 yaitu menghentingkan program dan print end message
    elif pilih == "4":
        print("Simulasi piket selesai. Sampai jumpa!")
        break
    else:
        print("Menu tidak valid.")

