class Kendaraan:
    def __init__(self, merk, nama, tahun, cc_mesin):
        self.merk = merk 
        self.nama = nama
        self.tahun = tahun 
        self.cc_mesin = cc_mesin 

    def tampilkan_info(self):
        print("Tampilkan Info Kendaraan")
        print("Merk Kendaraan  :", self.merk)
        print("Nama Kendaraan  :", self.nama)
        print("Tahun Kendaraan :", self.tahun)
        print("Kapasitas Mesin :", self.cc_mesin, "cc")

class Mobil(Kendaraan): 
    def __init__(self, merk, nama, tahun, cc_mesin, jumlah_kursi):
        super().__init__(merk, nama, tahun, cc_mesin)
        self.jumlah_kursi = jumlah_kursi

    def tampilkan_info(self):
        super().tampilkan_info()
        print("Jumlah Kursi    :", self.jumlah_kursi)

class Motor(Kendaraan):
    def __init__(self, merk, nama, tahun, cc_mesin, tipe_motor):
        super().__init__(merk, nama, tahun, cc_mesin)
        self.tipe_motor = tipe_motor

    def tampilkan_info(self):
        super().tampilkan_info()
        print("Tipe Motor      :", self.tipe_motor)


#Object Mobil 
mobil1 = Mobil(
    "Avanza",
    "Toyota",
    2023,
    1500,
    7
)

mobil2 = Mobil(
    "Innova",
    "Toyota",
    2022,
    2000,
    7
)

mobil3 = Mobil (
    "Agya",
    "Toyota",
    2023,
    1200,
    7
)

#Object Motor
motor1 = Motor(
    "Vario",
    "Honda", 
    2024,
    125, 
    "Matic"
)

motor2 = Motor(
    "Beat", 
    "Honda", 
    2023,
    120, 
    "Matic"
)

motor3 = Motor(
    "NMAX", 
    "Yamaha", 
    2022, 
    155, 
    "Matic"
)

print("Data Mobil")
mobil1.tampilkan_info()

print("\nData Motor")
motor1.tampilkan_info()
