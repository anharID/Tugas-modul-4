class sisa_stock:

    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

    def fstock (self, merk, size):
        if merk == "IMP":
            if size == "s" or "S":
                stock = 12
            elif size == "m" or "M":
                stock = 24
            elif size == "l" or "L":
                stock = 3
        elif merk == "Prada":
            if size == "s" or "S":
                stock = 17
            elif size == "m" or "M":
                stock = 43
            elif size == "l" or "L":
                stock = 34
        elif merk == "Gucci":
            if size == "s" or "S":
                stock = 10
            elif size == "m" or "M":
                stock = 24
            elif size == "l" or "L":
                stock = 4
        elif merk == "Louis Vuitton":
            if size == "s" or "S":
                stock = 15
            elif size == "m" or "M":
                stock = 13
            elif size == "l" or "L":
                stock = 6
        return stock
 
    def stock0 (self):
        print ("===============SISA STOCK BARANG==============")
        print (f"1. Stock total merk IMP           = {self.p1}")
        print (f"2. Stock total merk Prada         = {self.p2}")
        print (f"3. Stock total merk Gucci         = {self.p3}")
        print (f"4. Stock total merk Louis Vuitton = {self.p4}")
        print ("untuk info stock yang lebih rinci silahkan pilih merk dan size yang diinginkan pada MENU")
