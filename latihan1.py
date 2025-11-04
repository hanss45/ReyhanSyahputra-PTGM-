# Deklarasi Class
class Siswa:
    #Atribut Class
    sekolah = "SMK PGRI 35 Solokanjeruk"

    #Konstruktor
    def __init__(self, nama, nis, kelas_siswa):
        # Atribut Instance (Data unik per objek)
        self.nama = nama
        self.nis = nis
        self.kelas_siswa = kelas_siswa

    #Method 
    def tampilkan_profil_siswa(self):
        print("--- Profil Siswa ---")
        print(f"Nama Siswa  : {self.nama}")
        print(f"NIS         : {self.nis}")
        print(f"Kelas       : {self.kelas_siswa}")
        # Memanggil Atribut Class menggunakan nama Class (Siswa.sekolah)
        print(f"Sekolah     : {Siswa.sekolah}")
        print("--------------------")

# Membuat Objek
s1 = Siswa("Agus Setiawan", "10203001", "XII RPL")
s2 = Siswa("Budi Santoso", "10203002", "X TKJ")

# Memanggil Method 
s1.tampilkan_profil_siswa()
s2.tampilkan_profil_siswa()