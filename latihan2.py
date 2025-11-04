class Kendaraan:
    def __init__(self, merk, kecepatan):
        self.merk = merk
        self.kecepatan = kecepatan

    def info(self):
        print("Kendaraan bergerak...")
        
class Mobil(Kendaraan):
    def info(self):
        print(f"Mobil {self.merk} melaju {self.kecepatan} km/jam.")

class Motor(Kendaraan):
    def info(self):
        print(f"Motor {self.merk} melaju {self.kecepatan} km/jam.")

# Membuat objek dari subclass
mbl1 = Mobil("Toyota", 180)
mtr1 = Motor("Yamaha", 100)

# Memanggil method info()
mbl1.info()
mtr1.info()