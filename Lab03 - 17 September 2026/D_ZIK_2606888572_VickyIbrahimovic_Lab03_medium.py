

# Input Jumlah kucing dan konversi ke integer
n  = int(input("Masukkan jumlah kucing: "))
# Input Jumlah sisa nasi dan konversi ke integer
sisa_nasi = int(input("Masukkan sisa nasi (suap): "))

# Perulangan berdasarkan jumlah kucing
for kucing in range(1,n+1):
    # Input Level Kelaparan Kucing dan konversi ke integer
    level = int(input(f"Masukkan level kelaparan kucing ke-{kucing}: "))

    # Percabangan Jika level Kelaparan diatas 6
    if level > 6:
        # Percabangan Jika Nasi tidak cukup maka break
        if sisa_nasi < 3:
            print(f"Kucing {kucing}: nasi gak cukup, kabur!")
            break
        # Pengurangan Sisa Nasi sebesar 3 suap serta print laporan
        sisa_nasi -= 3
        print(f"Kucing {kucing}: dikasih 3 suap. Sisa nasi: {sisa_nasi}")
    
    # Percabangan Jika level Kelaparan diantara 3 dan 6 secara eksklusif
    elif level >= 3 and level <= 6:
        # Percabangan Jika Nasi tidak cukup maka break
        if sisa_nasi < 1:
            print(f"Kucing {kucing}: nasi gak cukup, kabur!")
            break
        # Pengurangan Sisa Nasi sebesar 1 suap serta print laporan
        sisa_nasi -= 1
        print(f"Kucing {kucing}: dikasih 1 suap. Sisa nasi: {sisa_nasi}")
    
    # Percabangan jika percabangan diatas belum memenuhi
    else:
        # Print Laporan kucing jika tidak dikasih nasi
        print(f"Kucing {kucing}: gak dikasih. Sisa nasi: {sisa_nasi}")
    
