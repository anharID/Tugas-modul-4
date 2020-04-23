ulang = str
while ulang:
    print ("PROGRAM CEK HARGA\n")
    print ("MERK YANG TERSEDIA\n 1.IMP\n 2.Prada\n 3.Gucci\n 4.Louis Vuitton\n")
    print ("Size yang tersedia: s, m, l\n")
    print("masukan pilihan anda: ")
    pilihan = int(input())
    print("masukan size yang diinginkan: ")
    size = input()
    if pilihan == 1:
        merk = "IMP"
        if size == "s":
            harga = 150000
        elif size == "m":
            harga = 200000
        elif size == "l":
            harga = 250000
        print("merk: ", merk)
        print("size: ", size)
        print("harga: ", harga)
        print()

    elif pilihan == 2:
        merk = "Prada"
        if size == "s":
            harga = 150000
        elif size == "m":
            harga = 160000
        elif size == "l":
            harga = 170000
        print("merk: ", merk)
        print("size: ", size)
        print("harga: ", harga)
        print()
    elif pilihan == 3:
        merk = "Gucci"
        if size == "s":
            harga = 200000
        elif size == "m":
            harga = 210000
        elif size == "l":
            harga = 230000
        print("merk: ", merk)
        print("size: ", size)
        print("harga: ", harga)
        print()
    elif pilihan == 4:
        merk = "Louis Vuitton"
        if size == "s":
            harga = 300000
        elif size == "m":
            harga = 300000
        elif size == "l":
            harga = 350000
        print("merk: ", merk)
        print("size: ", size)
        print("harga: ", harga)
        print()
    else:
        print ("pilihan tidak tersedia")
        print()
           
    print("Apakah anda ingin mengulang program? (Y/T)")
    ulang1 = input()
    print("\n")
    if ulang1 == "T":
        print("terima kasih telah menggunakan program")
        break
