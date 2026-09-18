# Input fokus awal yang dikonversi ke integer
fokus_awal  = int(input("Masukkan level fokus awal: "))

# Input jumlah konten yang dikonversi ke integer
jumlah_konten  = int(input("Masukkan jumlah konten yang di-scroll:  "))

# Perulangan berdasarkan jumlah konten
for konten in range(1,jumlah_konten+1):
    # Input Kode Konten
    kode_konten = int(input(f"Masukkan kode konten ke-{konten} (1/2/3): "))

    # Logika Percabangan Fokus sebesar berkurang 5 jika kode konten 1
    if kode_konten == 1:
        fokus_awal -= 5
    # Logika Percabangan Fokus sebesar berkurang 15 jika kode konten 2
    elif kode_konten == 2:
        fokus_awal -= 15
    # Logika Percabangan Fokus sebesar bertambah 20 jika kode konten 3
    elif kode_konten == 3:
        fokus_awal += 20

    # Mengembalikan Nilai fokus awal ke 0 jika nilai fokus awal dibawah 0
    if fokus_awal < 0:
        fokus_awal = 0
    # Mengembalikan Nilai fokus awal ke 100 jika nilai fokus awal melebihi 100
    elif fokus_awal > 100:
        fokus_awal = 100

# Print Fokus Akhir
print(f"Fokus akhir: {fokus_awal}")

# Print Status yang bergantung dari nilai fokus awal
if fokus_awal == 0:
    print("Status : Otak Kosong")
elif fokus_awal> 0 and fokus_awal < 20:
    print("Status : Butuh Healing")
else:
    print("Status : Masih Waras")



