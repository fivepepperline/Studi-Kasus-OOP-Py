class Dosen:
    def __init__(self, nidn, nama, prodi, fakultas):
        self.nidn = nidn
        self.nama = nama
        self.prodi = prodi
        self.fakultas = fakultas

    def tampilkan_profil(self):
        print("Tampilkan Info Dosen")
        print("NIDN     :", self.nidn)
        print("Nama     :", self.nama)
        print("Fakultas :", self.fakultas)
        print()

    def cek_prodi(self):
        if self.prodi == "S1 Matematika":
            print("Dosen berasal dari Prodi S1 Matematika")
        elif self.prodi == "S1 Biologi":
            print("Dosen berasal dari Prodi S1 Biologi")
        elif self.prodi == "S1 Fisika":
            print("Dosen berasal dari Prodi S1 Fisika")
        else:
            print("Prodi tidak terdaftar")
        print()


dosen1 = Dosen(
    1009223401,
    "Buidanto Fernandez",
    "S1 Matematika",
    "Fakultas Ilmu Pendidikan"
)

dosen2 = Dosen(
    1009223403,
    "Sutris Garcia",
    "S1 Biologi",
    "Fakultas Ilmu Pendidikan"
)

dosen3 = Dosen(
    10092253018,
    "Agus Martinez",
    "S1 Fisika",
    "Fakultas Teknik"
)

dosen1.tampilkan_profil()
dosen2.tampilkan_profil()
dosen3.tampilkan_profil()

dosen1.cek_prodi()
dosen2.cek_prodi()
dosen3.cek_prodi()

