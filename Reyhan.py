print("=== KALKULATOR SEDERHANA ===")

ulang = "y"
while ulang.lower() == "y":
    print("\nPilih operasi:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    print("5. Keluar")

    pilihan = input("Masukkan pilihan (1-5): ")

    if pilihan == '5':
        print("Terima kasih! Program selesai.")
        break

    try:
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
    except ValueError:
        print("Input tidak valid! Masukkan angka saja.")
        continue

    if pilihan == '1':
        hasil = a + b
        operasi = "+"
    elif pilihan == '2':
        hasil = a - b
        operasi = "-"
    elif pilihan == '3':
        hasil = a * b
        operasi = "*"
    elif pilihan == '4':
        if b == 0:
            print("Error: Tidak bisa membagi dengan nol!")
            continue
        hasil = a / b
        operasi = "/"
    else:
        print("Pilihan tidak valid! Silakan pilih 1-5.")
        continue

    # ubah hasil ke int jika tidak ada desimal
    if hasil.is_integer():
        hasil = int(hasil)
    if a.is_integer():
        a = int(a)
    if b.is_integer():
        b = int(b)

    print("Hasil dari", a, operasi, b, "=", hasil)

    ulang = input("\nIngin menghitung lagi? (y/n): ")
    