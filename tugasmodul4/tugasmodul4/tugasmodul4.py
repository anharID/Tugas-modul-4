import percobaan2
import percobaan3

def perkenalan(nama1, nama2, kelompok):
    print (f"ini adalah program yang dibut oleh {nama1} dan {nama2} dari kelompok {kelompok}")
perkenalan("Anhar", "Rifki", 25)

p1 = percobaan2.pemethod("Anhar", 21120119120012)
p1.iden1()
p2 = percobaan2.pemethod("Rifki Satriamas", 21120119130115)
p2.iden2()
p3 = percobaan3.sisa_stock(39, 94, 38, 34)



def fharga (merk, size):
    if merk == "IMP":
        if size == "s" or "S":
            harga = 150000
        elif size == "m" or "M":
            harga = 200000
        elif size == "l" or "L":
            harga = 250000
    elif merk == "Prada":
        if size == "s" or "S":
            harga = 150000
        elif size == "m" or "M":
            harga = 160000
        elif size == "l" or "L":
            harga = 170000
    elif merk == "Gucci":
        if size == "s" or "S":
            harga = 200000
        elif size == "m" or "M":
            harga = 210000
        elif size == "l" or "L":
            harga = 230000
    elif merk == "Louis Vuitton":
        if size == "s" or "S":
            harga = 300000
        elif size == "m" or "M":
            harga = 300000
        elif size == "l" or "L":
            harga = 350000
    return harga

ulang = str
while ulang:
    print ("===============PROGRAM CEK HARGA===============\n")
    print ("MENU YANG TERSEDIA : \n 1.IMP\n 2.Prada\n 3.Gucci\n 4.Louis Vuitton\n 5.CEK STOCK SEMUA BARANG\n 6.KELUAR PROGRAM\n")
    print ("Size yang tersedia: S, M, L\n")
    pilihan = int(input("masukan pilihan anda: "))
    if pilihan == 1:
        merk = "IMP"
        size = input("masukan size yang diinginkan: ")
        harga = fharga (merk, size)
        stock = p3.fstock(merk, size)
        print("merk: ", merk)
        print("size: ", size)
        print("sisa produk: ", stock)
        print("harga: ", harga)
        print()
    elif pilihan == 2:
        merk = "Prada"
        size = input("masukan size yang diinginkan: ")
        harga = fharga (merk, size)
        stock = p3.fstock(merk, size)
        print("merk: ", merk)
        print("size: ", size)
        print("sisa produk: ", stock)
        print("harga: ", harga)
        print()
    elif pilihan == 3:
        merk = "Gucci"
        size = input("masukan size yang diinginkan: ")
        harga = fharga (merk, size)
        stock = p3.fstock(merk, size)
        print("merk: ", merk)
        print("size: ", size)   
        print("sisa produk: ", stock)
        print("harga: ", harga)
        print()
    elif pilihan == 4:
        merk = "Louis Vuitton"
        size = input("masukan size yang diinginkan: ")
        harga = fharga (merk, size)
        stock = p3.fstock(merk, size)
        print("merk: ", merk)
        print("size: ", size)
        print("sisa produk: ", stock)
        print("harga: ", harga)  
        print()
    elif pilihan == 5:
        p3.stock0()
        print()
    elif pilihan == 6:
        print ("terima kasih telah menggunakan program kami\n")
        break
    else:
        print ("pilihan tidak tersedia")
        print()
           

