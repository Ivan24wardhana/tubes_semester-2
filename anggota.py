import os
from tabulate import tabulate

class Anggota:
    def __init__(self, id_anggota, nama, alamat, no_telp, tgl_daftar= None):
        self.id_anggota = id_anggota
        self.nama = nama
        self.alamat = alamat
        self.no_telp = no_telp
        self.tgl_daftar = tgl_daftar

    def tampilkan_anggota(self):
        print(f"ID Anggota   : {self.id_anggota}")
        print(f"Nama         : {self.nama}")
        print(f"Alamat       : {self.alamat}")
        print(f"No. Telp     : {self.no_telp}")
        print(f"Tgl Daftar   : {self.tgl_daftar}")
        print()
        
def baca_file_anggota():
    daftar_anggota = []
    try:
        path_file = os.path.join(os.path.dirname(__file__), "anggota.txt")
        if os.path.exists(path_file):
            with open(path_file, "r") as file:
                for line in file:
                    id_anggota, nama, alamat, no_telp, tgl_daftar = line.strip().split(",")
                    daftar_anggota.append(Anggota(id_anggota, nama, alamat, no_telp, tgl_daftar))
    except FileNotFoundError:
        print("Belum ada data anggota.")
        input("Tekan enter untuk kembali...")
    return daftar_anggota

def tampilkan_daftar_anggota():
    path_file = os.path.join(os.path.dirname(__file__), "anggota.txt")
    daftar_anggota = []

    try:
        if os.path.exists(path_file):
            with open(path_file, "r") as file:
                for line in file:
                    id_anggota, nama, alamat, no_telp, tgl_daftar = line.strip().split(",")
                    daftar_anggota.append([id_anggota, nama, alamat, no_telp, tgl_daftar])
        else:
            print("Belum ada data anggota.")
            return
    except Exception as e:
        print(f"Terjadi kesalahan saat membaca file: {e}")
        return

    headers = ["ID Anggota", "Nama", "Alamat", "No. Telp", "Tgl Daftar"]

    print("\n=== Daftar Anggota ===")
    print(tabulate(daftar_anggota, headers=headers, tablefmt="grid"))

    
