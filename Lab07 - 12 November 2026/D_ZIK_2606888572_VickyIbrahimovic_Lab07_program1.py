def hitung_cara(sisa_blok, sebelumnya_dua):
    # Percabangan ketika semua blok berhasil dicadangkann
    if sisa_blok == 0:
        return 1
    if sisa_blok < 0:
        return 0

    # Menghitung banyak cara jika proses berikutnya mencadangkan satu blok.
    jumlah_cara = hitung_cara(sisa_blok - 1, False)

    # Menghitung untuk tambahkan kemungkinan mencadangkan dua blok sekaligus.
    if not sebelumnya_dua:
        jumlah_cara += hitung_cara(sisa_blok - 2, True)

    # Return Jumlah seluruh cara
    return jumlah_cara

# Fungsi Print Header
print("=== SISTEM PENCADANGAN DATA AKADEMIK ===")
# Mengintput Jumlah blok data
n = int(input("Masukkan jumlah blok data: "))
# Menghitung banyak cara
hasil = hitung_cara(n, False)
# Print Hasil Analisis
print("\n=== HASIL ANALISIS ===")
print(f"Untuk {n} blok data, terdapat {hasil} cara pencadangan yang valid.")