import os
from tabulate import tabulate
from Buku.buku import Buku
from Anggota.anggota import Anggota

class Peminjam(Anggota, Buku):
    def __init__(self, id_peminjam, anggota: Anggota, buku: Buku, tgl_pinjam, tgl_kembali):
        Anggota.__init__(self, anggota.id_anggota, anggota.nama, anggota.alamat, anggota.no_telp)
        Buku.__init__(self, buku.id_buku, buku.judul, buku.penulis, buku.tahun_terbit)
        self.id_peminjam = id_peminjam
        self.tgl_pinjam = tgl_pinjam
        self.tgl_kembali = tgl_kembali

    def tampilkan_peminjam(self):
        print(f"ID Peminjam     : {self.id_peminjam}")
        print(f"ID Anggota      : {self.id_anggota}")
        print(f"Nama            : {self.nama}")
        print(f"Alamat          : {self.alamat}")
        print(f"No. Telepon     : {self.no_telp}")
        print(f"ID Buku         : {self.id_buku}")
        print(f"Judul Buku      : {self.judul}")
        print(f"Penulis         : {self.penulis}")
        print(f"Tahun Terbit    : {self.tahun_terbit}")
        print(f"Tanggal Pinjam  : {self.tgl_pinjam}")
        print(f"Tanggal Kembali : {self.tgl_kembali}")

def baca_file_peminjam():
    daftar_peminjam = []
    try:
        path_file = os.path.join(os.path.dirname(__file__), "peminjam.txt")
        with open(path_file, "r") as file:
            for line in file:
                id_peminjam, id_anggota, nama, alamat, no_telp, id_buku, judul, penulis, tahun_terbit, tgl_pinjam, tgl_kembali = line.strip().split(",")
                anggota = Anggota(id_anggota, nama, alamat, no_telp)
                buku = Buku(id_buku, judul, penulis, tahun_terbit)
                daftar_peminjam.append(Peminjam(id_peminjam, anggota, buku, tgl_pinjam, tgl_kembali))
    except FileNotFoundError:
        print("Belum ada data peminjam.")
    return daftar_peminjam

def tampilkan_daftar_peminjam():
    path_file = os.path.join(os.path.dirname(__file__), "peminjam.txt")
    daftar_peminjam = []
    try:
        if os.path.exists(path_file):
            with open(path_file, "r") as file:
                for line in file:
                    id_peminjam, id_anggota, nama, alamat, no_telp, id_buku, judul, penulis, tahun_terbit, tgl_pinjam, tgl_kembali = line.strip().split(",")
                    daftar_peminjam.append([id_peminjam, id_anggota, nama, alamat, no_telp, id_buku, judul, penulis, tahun_terbit, tgl_pinjam, tgl_kembali])
        else:
            print("Belum ada data anggota.")
            return
    except Exception as e:
        print(f"Terjadi kesalahan saat membaca file: {e}")
        return

    headers = ["ID Peminjam", "ID Anggota", "Nama", "Alamat", "No.Telp", "ID Buku", "Judul Buku", "Penulis", "Tahun Terbit", "Pinjam", "Kembali"]

    print("\n=== Daftar Peminjam ===")
    print(tabulate(daftar_peminjam, headers=headers, tablefmt="grid", colalign=("center",) * len(headers), maxcolwidths=[None, None, 10, 15, 10, None, 20, 12, None, None, None]))
