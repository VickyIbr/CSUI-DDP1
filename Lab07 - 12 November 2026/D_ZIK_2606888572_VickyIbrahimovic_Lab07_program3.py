def matkul_diambil(mk):
    """
    Mengembalikan list MK yang dapat diambil semester depan
    sebagai langkah menuju mk.

    Variabel yang dapat digunakan:
    - lulus     : list kode MK yang sudah lulus
    - prasyarat : dictionary {kode MK: list kode prasyaratnya}
                  MK tanpa prasyarat tidak ada di dictionary ini.
    """ 
    # Menangani kondisi ketika mk sudah lulus.
    if mk in lulus:
        return []

    # Kumpulkan MK yang dapat diambil semester depan dari setiap prasyarat mk.
    hasil = []
    for p in prasyarat.get(mk, []):
        hasil.extend(matkul_diambil(p))

    # Percabganan Jika tidak ada MK yang perlu diambil lebih dulu, mk sendiri dapat diambil semester depan.
    if not hasil:
        return [mk]
    
    # FUngsi untuk return hasil
    return hasil


# ===== Program utama =====

# Input dan Proses Matkul
target = input()
lulus = input().split()
prasyarat = {}

# Membaca M, lalu menyimpan M baris data prasyarat ke dict prasyarat. Kata pertama setiap baris menjadi key, sisanya menjadi value.
m = int(input())
for i in range(m):
    baris = input().split()
    prasyarat[baris[0]] = baris[1:]

# Memanggil matkul_diambil(target), membuang MK yang muncul lebih dari sekali, Mengurutkan secara abjad, lalu cetak sesuai format output.
hasil = sorted(set(matkul_diambil(target)))
print(f"Semester depan: {', '.join(hasil)}")