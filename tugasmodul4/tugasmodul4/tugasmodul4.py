def fharga (merk, size):
    if merk == "IMP":
        if size == "s":
            harga = 150000
        elif size == "m":
            harga = 200000
        elif size == "l":
            harga = 250000
    elif merk == "Prada":
        if size == "s":
            harga = 150000
        elif size == "m":
            harga = 160000
        elif size == "l":
            harga = 170000
    elif merk == "Gucci":
        if size == "s":
            harga = 200000
        elif size == "m":
            harga = 210000
        elif size == "l":
            harga = 230000
    elif merk == "Louis Vuitton":
        if size == "s":
            harga = 300000
        elif size == "m":
            harga = 300000
        elif size == "l":
            harga = 350000
    return harga

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
        harga = fharga (merk, size)
        print("merk: ", merk)
        print("size: ", size)
        print("harga: ", harga)
        print()
    elif pilihan == 2:
        merk = "Prada"
        harga = fharga (merk, size)
        print("merk: ", merk)
        print("size: ", size)
        print("harga: ", harga)
        print()
    elif pilihan == 3:
        merk = "Gucci"
        harga = fharga (merk, size)
        print("merk: ", merk)
        print("size: ", size)
        print("harga: ", harga)
        print()
    elif pilihan == 4:
        merk = "Louis Vuitton"
        harga = fharga (merk, size)
        print("merk: ", merk)
        print("size: ", size)
        print("harga: ", harga)
        print()
    else:
        print ("pilihan tidak tersedia")
        print()
           
    print("Apakah anda ingin mengulang program? (Y/T)")
    ulang = input()
    print("\n")
    if ulang == "t":
        break
