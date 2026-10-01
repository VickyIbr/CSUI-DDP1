# Membuka File sensor mentah untuk read, cuaca_rapi dan error log untuk append
file_input = open("sensor_mentah.txt")
file_output = open("cuaca_rapi.txt", "a")
file_error = open("error.log", "a")
count_valid = 0

pemisah = "|"

#perulangan untuk membaca data dari file teks sensor_mentah baris demi baris.
for line in file_input:
    valid = True

    # Pemisahahan Line berdasarkan | dengan split
    list_line = line.split("|")
    date = list_line[0].strip()
    lokasi = list_line[1].strip()
    cuaca = list_line[2].strip()

    # Membersihkan Data Lokasi dari spasi berlebih dan dikapitalisasi
    new_lokasi = " ".join(lokasi.split()).title()

    #Format Tanggal pada data mentah YYYY-MM-DD menjadi dipisahkan oleh /.
    list_date = date.split("-")
    day = list_date[2]
    month = list_date[1]
    year = list_date[0]
    new_date = day+"/"+month+"/"+year

    #MeLakukan pengecekan terhadap komponen Log Cuaca untuk mendeteksi data yang rusak. Jika rusak assign valid dengan nilai False
    for i in cuaca:
        if i not in("CHM"):
            valid = False

    #Jika data valid (tidak rusak) melakukan Run-Length Encoding di cuaca
    if valid:
        # Assign Temporary Cuaca dan Current Char untuk keperluan kompresi
        temp = []
        current_char = cuaca[0]
        count = 1
        # Perulangan untuk cek char dari cuaca,
        for char in cuaca[1:]:
            # jika sama count +1
            if char == current_char:
                count += 1
            # Jika Karakter berbeda artinya, huruf selesai dihitung dan siap dikompresi
            else:
                # append jumlah huruf dan hurufnya
                temp.append(f"{count}{current_char}")
                # Ganti Current char dengan char baru yang berbeda
                current_char = char
                # Reset Count ke 1
                count = 1
        temp.append(f"{count}{current_char}")
        # List yang ada di temp digabungkan semua di new cuaca hasil kompresi
        new_cuaca = "".join(temp)

        # Format File output yang akan di tulis ke file
        file_output.write(f"{new_date} - {new_lokasi}: {new_cuaca}\n")
        # Penghitungan data tervalidasi
        count_valid += 1
    else:
        # Write Erorr log jika data rusak
        file_error.write(f"Data rusak pada {new_date} di {new_lokasi} dengan log cuaca {cuaca}.\n")


#cetak ke layar terminal total data yang berhasil diproses secara valid.
print(f"Total data valid: {count_valid}")

# Close Semua File
file_input.close()
file_error.close()
file_output.close()