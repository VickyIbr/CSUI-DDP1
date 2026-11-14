# Inisialisasi Mata Kuliah
class MataKuliah:

    # Constructor pembuat object dengan class mata kuliah
    def __init__(self, kode, nama, sks):
        self.kode = kode
        self.nama = nama
        self.sks = sks

    # Method untuk menghitung durasi mata kuliah
    def hitung_durasi(self):
        return sks*50

    # Method untuk menampilkan Informasi mengenai mata kuliah
    def tampilkan_info(self):
        print(f"""Kode: {self.kode}
Nama: {self.nama}
Jumlah SKS: {self.sks}
Durasi perkuliahan: {self.hitung_durasi()} menit
""")

# Print header dan input mengenai mata kuliah
print("=== INFORMASI MATA KULIAH ===")
kode = input("Masukkan kode mata kuliah: ")
nama = input("Masukkan nama mata kuliah: ")
sks = int(input("Masukkan jumlah SKS: "))

# Membuat Objek Mata kuliah
mata_kuliah = MataKuliah(kode,nama,sks)

# Print dan penggunaan method untuk menampilakan informasi mengenai objek yang telah dibuat
print("\n=== RINCIAN MATA KULIAH ===")
mata_kuliah.tampilkan_info()
