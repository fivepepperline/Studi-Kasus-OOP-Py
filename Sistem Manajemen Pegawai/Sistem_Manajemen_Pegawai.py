class Pegawai:
    def __init__(self, id_pegawai, nama, jabatan, **kwargs):
        self.id_pegawai = id_pegawai
        self.nama = nama 
        self.jabatan = jabatan

class Gaji: 
    def __init__(self, gaji, **kwargs):
        self.gaji = gaji 


class PegawaiProyek: 
    def __init__(self, nama_proyek, **kwargs):
        self.nama_proyek = nama_proyek

class ProjectManager(Pegawai, Gaji, PegawaiProyek):
    def __init__(self, id_pegawai, nama, jabatan, gaji, nama_proyek):
        Pegawai.__init__(self, id_pegawai, nama, jabatan)
        Gaji.__init__(self, gaji)
        PegawaiProyek.__init__(self, nama_proyek)

    def tampilkan_profil(self):
        return {
            "ID Pegawai": self.id_pegawai,
            "Nama": self.nama,
            "Jabatan": self.jabatan,
        }

    def hitung_gaji(self):
        return self.gaji

    def info_proyek(self):
        return f"{self.nama} memimpin proyek '{self.nama_proyek}' dengan gaji Rp{self.gaji:,.0f}."


PM1 = ProjectManager(
    id_pegawai = "00901",
    nama = "Santoso",
    jabatan = "Supervisor", 
    gaji = 5000000, 
    nama_proyek = "Rumah Subsidi"
)

PM2 = ProjectManager(
    id_pegawai = "00902",
    nama = "Sutrisno",
    jabatan = "Worker", 
    gaji = 3000000, 
    nama_proyek = "Rumah Subsidi"
)

print("ID_pegawai :", PM1.id_pegawai)
print("Nama       :", PM1.nama)
print("Jabatan    :", PM1.jabatan)
print("Gaji       :",PM1.gaji)
print("Nama Proyek:", PM1.nama_proyek)
print()
print("ID_pegawai :", PM2.id_pegawai)
print("Nama       :", PM2.nama)
print("Jabatan    :", PM2.jabatan)
print("Gaji       :", PM2.gaji)
print("Nama Proyek:", PM2.nama_proyek)