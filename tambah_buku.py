from Buku.buku import Buku, BukuFiksi, BukuNonFiksi, baca_file_buku
import os

def tambah_buku():
    id_buku      = input("Masukkan ID Buku           : ")
    judul        = input("Masukkan Judul Buku        : ")
    penulis      = input("Masukkan Penulis Buku      : ")
    tahun_terbit = input("Masukkan Tahun Terbit Buku : ")
    stok         = input("Masukkan Jumlah Stok Buku  : ")

    jenis = input("Jenis Buku (fiksi/nonfiksi): ").lower()
    if jenis == "fiksi":
        genre = input("Masukkan Genre Buku Fiksi      : ")
        buku_baru = BukuFiksi(id_buku, judul, penulis, tahun_terbit, genre, stok)
        simpan_buku(buku_baru, jenis)
    elif jenis == "nonfiksi":
        kategori = input("Masukkan Kategori Buku Non-Fiksi: ")
        buku_baru = BukuNonFiksi(id_buku, judul, penulis, tahun_terbit, kategori, stok)
        simpan_buku(buku_baru, jenis)
    else:
        print("Jenis buku tidak valid.")
        return

    print("\nData buku berhasil ditambahkan.")
    lanjut_edit = input("Apakah ingin tambah buku lain? (y/n): ").lower()
    if lanjut_edit == "y":
        tambah_buku()
    else:
        input("Tekan Enter untuk kembali...")
    return
    

def simpan_buku(buku, jenis):
    path_file = os.path.join(os.path.dirname(__file__), "buku.txt")
    with open(path_file, "a") as file:
        if isinstance(buku, BukuFiksi):
            file.write(f"{jenis},{buku.id_buku},{buku.judul},{buku.penulis},{buku.tahun_terbit},{buku.genre},{buku.stok}\n")
        elif isinstance(buku, BukuNonFiksi):
            file.write(f"{jenis},{buku.id_buku},{buku.judul},{buku.penulis},{buku.tahun_terbit},{buku.kategori},{buku.stok}\n")
        
