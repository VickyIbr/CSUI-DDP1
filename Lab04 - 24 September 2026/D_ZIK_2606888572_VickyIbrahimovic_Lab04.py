# =====================================================================
# Nama  : Vicky Ibrahimovic
# NPM   : 2606888572
# Kelas : D
# =====================================================================
# Kerjakan setiap TODO di bawah sesuai dengan spesifikasi soal Lab 04.
# =====================================================================

print("=== POUPET SIMULATOR ===")

# Inisialisasi status awal PouPet
kenyang = 40
mood = 40

# Loop utama
while True:
    makanan = input("Beri makan PouPet: ")

    # logika untuk cek kata mengandung "TIDUR" serta untuk print dan menghentikan program
    if makanan == "TIDUR":
        print("PouPet tertidur pulas… Sampai jumpa!")
        break

    # Hitung efek setiap karakter terhadap status kenyang dan mood serta melakukan pembersihan makanan ke dalam variabel penampung string bersih

    # Inisialisasi Makanan Bersih
    makanan_bersih = ""

    # Perulangan setiap char di makanan
    for char in makanan:
        # Percabangan Jika Vokal
        if char.upper() in "AIUEO":
            kenyang += 5
            makanan_bersih += char.upper()
        # Percabangan Jika Konsonan
        elif char.upper() in "BCDFGHJKLMNPQRSTVWXYZ":
            mood += 3
            makanan_bersih += char.lower()
        # Percabangan Jika bukan Alphabet
        else:
            kenyang -= 5
            mood -= 5

    # Mencetak status makanan di piring berdasarkan alphabet
    if makanan_bersih.isalpha() == True:
        print(f"Makanan di piring: {makanan_bersih}")
    else:
        print("Makanan di piring: (piring kosong, semua dibuang)")

    #Cek kemunculan huruf alfabet yang sama secara berurutan minimal 3 kali
    #Inisialisasi Counter dan Temp untuk membantu cek huruf alfabet yang sama
    counter = 1
    temp = 0
    for char in makanan_bersih:
        if char == temp:
            counter +=1
        else:
            counter = 1
        if counter == 3:
            mood -= 15
            print("Huwek! Terlalu banyak huruf berulang")
            break
        temp = char

    #Cek apakah string bersih merupakan palindrom (panjang minimal 2 karakter).
    #Inisialisasi Kata Terbalik
    terbalik = ""
    if len(makanan_bersih) >=2:
        for char in makanan_bersih:
            terbalik = char + terbalik
        if terbalik == makanan_bersih:
            print(f"NYAM! Palindrom {makanan_bersih} lezat!")
            mood += 20

    # Logika untuk Membatasi Kenyang di range 0 -100
    if kenyang > 100:
        kenyang = 100
    elif kenyang < 0:
        kenyang = 0

    # Logika untuk Membatasi Mood di range 0 -100
    if mood > 100:
        mood = 100
    elif mood < 0:
        mood = 0


    #Mencetak progress bar dan nilai status terbaru untuk kenyang dan mood.

    # Insialisasi karakter Bar Kenyang
    bar_kenyang = (kenyang//10*"#") + ((10 - kenyang//10) * "-")
    # Insialisasi karakter Bar Mood
    bar_mood = (mood//10*"#") + ((10 - mood//10) * "-")

    # Mencetak Berdasarkan bar kenyang dan bar mood
    print(f"Kenyang: [{bar_kenyang}] {kenyang}/100 | Mood: [{bar_mood}] {mood}/100")

    # Logika Game Over jika kenyang dan mood kurang dari 0
    if kenyang <= 0 and mood <= 0:
        print("Game Over! PouPet kelaparan dan marah")
        break
    elif kenyang <= 0:
        print("Game Over! PouPet kelaparan")
        break
    elif mood <= 0:
        print("Game Over! PouPet marah")
        break
    # Print newline untuk kerapihan output (menyesuaikan contoh interaksi di dokumen lab)
    print("")