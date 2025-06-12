import os
from tabulate import tabulate

class Buku:
    def __init__(self, id_buku, judul, penulis, tahun_terbit, stok=0):
        self.id_buku = id_buku
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit
        self.stok = int(stok)

    def tampilkan_buku(self):
        print(f"ID Buku   : {self.id_buku}")
        print(f"Judul     : {self.judul}")
        print(f"Penulis   : {self.penulis}")
        print(f"Tahun     : {self.tahun_terbit}")
        print(f"Stok      : {self.stok}")

class BukuFiksi(Buku):
    def __init__(self, id_buku, judul, penulis, tahun_terbit, genre, stok):
        super().__init__(id_buku, judul, penulis, tahun_terbit, stok)
        self.genre = genre

    def tampilkan_buku(self):
        super().tampilkan_buku()
        print(f"Genre     : {self.genre}\n")

class BukuNonFiksi(Buku):
    def __init__(self, id_buku, judul, penulis, tahun_terbit, kategori, stok):
        super().__init__(id_buku, judul, penulis, tahun_terbit, stok)
        self.kategori = kategori

    def tampilkan_buku(self):
        super().tampilkan_buku()
        print(f"Kategori  : {self.kategori}\n")

def baca_file_buku():
    daftar_buku = []
    path_file = os.path.join(os.path.dirname(__file__), "buku.txt")
    if os.path.exists(path_file):
        with open(path_file, "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == "fiksi" and len(data) == 7:
                    _, id_buku, judul, penulis, tahun, genre, stok = data
                    daftar_buku.append(BukuFiksi(id_buku, judul, penulis, tahun, genre, stok))
                elif data[0] == "nonfiksi" and len(data) == 7:
                    _, id_buku, judul, penulis, tahun, kategori, stok = data
                    daftar_buku.append(BukuNonFiksi(id_buku, judul, penulis, tahun, kategori, stok))
    return daftar_buku

def tampilkan_daftar_buku():
    path_file = os.path.join(os.path.dirname(__file__), "buku.txt")
    daftar_buku = []

    try:
        if os.path.exists(path_file):
            with open(path_file, "r") as file:
                for line in file:
                    data = line.strip().split(",")
                    if data[0] == "fiksi" and len(data) == 7:
                        _, id_buku, judul, penulis, tahun, genre, stok = data
                        daftar_buku.append([id_buku, judul, penulis, tahun, genre, stok])
                    elif data[0] == "nonfiksi" and len(data) == 7:
                        _, id_buku, judul, penulis, tahun, kategori, stok = data
                        daftar_buku.append([id_buku, judul, penulis, tahun, kategori, stok])
        else:
            print("Belum ada data buku.")
            return
    except Exception as e:
        print(f"Terjadi kesalahan saat membaca file: {e}")
        return

    headers = ["ID Buku", "Judul", "Penulis", "Tahun Terbit", "Genre/Kategori", "Stok"]

    print("\n=== Daftar Buku ===")
    print(tabulate(daftar_buku, headers=headers, tablefmt="grid"))

