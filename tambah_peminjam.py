from Peminjam.peminjam import Peminjam
from Buku.buku import baca_file_buku, BukuFiksi, BukuNonFiksi
from Anggota.anggota import Anggota
from Buku.buku import Buku
import datetime
import os

anggota_file = os.path.join("Anggota", "anggota.txt")
buku_file    = os.path.join("Buku", "buku.txt")

def tambah_peminjam():
    id_peminjam = "PJM" + datetime.datetime.now().strftime("%Y%m%d%H%M")
    id_anggota  = input("Masukkan ID Anggota     : ")
    id_buku     = input("Masukkan ID Buku        : ")
    tgl_pinjam  = datetime.date.today()
    tgl_kembali = tgl_pinjam + datetime.timedelta(days=7)

    # Cari data anggota
    anggota = None
    try:
        with open(anggota_file, "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0].strip() == id_anggota:
                    anggota = Anggota(data[0], data[1], data[2], data[3])
                    break
        if not anggota:
            print("ID Anggota tidak ditemukan.")
            return
    except FileNotFoundError:
        print("File anggota.txt tidak ditemukan.")
        return
    
    buku = None
    try:
        with open(buku_file, "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[1].strip() == id_buku:
                    buku = Buku(data[1], data[2], data[3], data[4])
                    break
        if not buku:
            print("ID Buku tidak ditemukan.")
            return
    except FileNotFoundError:
        print("File buku.txt tidak ditemukan.")
        return

    # Cari data buku
    daftar_buku = baca_file_buku()
    buku = None
    for b in daftar_buku:
        if b.id_buku == id_buku:
            buku = b
            if buku.stok > 0:
                buku.stok -= 1
            else:
                print("Stok buku habis, tidak bisa dipinjam.")
                input("Tekan Enter untuk kembali...")
                return
            break
    if not buku:
        print("ID Buku tidak ditemukan.")
        return

    # Update file buku.txt setelah stok berkurang
    with open(buku_file, "w") as f:
        for b in daftar_buku:
            if isinstance(b, BukuFiksi):
                f.write(f"fiksi,{b.id_buku},{b.judul},{b.penulis},{b.tahun_terbit},{b.genre},{b.stok}\n")
            else:
                f.write(f"nonfiksi,{b.id_buku},{b.judul},{b.penulis},{b.tahun_terbit},{b.kategori},{b.stok}\n")

    # Buat objek peminjam
    peminjam = Peminjam(id_peminjam, anggota, buku, tgl_pinjam, tgl_kembali)
    simpan_peminjam(peminjam)

    print("\nData peminjam berhasil ditambahkan.")
    lanjut_edit = input("Apakah ingin tambah peminjam lain? (y/n): ").lower()
    if lanjut_edit == "y":
        tambah_peminjam()
    else:
        input("Tekan Enter untuk kembali...")
    return


def simpan_peminjam(peminjam):
    path_file = os.path.join(os.path.dirname(__file__), "peminjam.txt")
    with open(path_file, "a") as file:
        file.write(f"{peminjam.id_peminjam},{peminjam.id_anggota},{peminjam.nama},{peminjam.alamat},{peminjam.no_telp},{peminjam.id_buku},{peminjam.judul},{peminjam.penulis},{peminjam.tahun_terbit},{peminjam.tgl_pinjam},{peminjam.tgl_kembali}\n")
