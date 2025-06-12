from Peminjam.peminjam import baca_file_peminjam
from Buku.buku import baca_file_buku, BukuFiksi, BukuNonFiksi
import datetime
import os

def kembali_peminjam():
    daftar_peminjam = baca_file_peminjam()
    if not daftar_peminjam:
        print("Belum ada peminjaman yang harus dikembalikan.")
        return

    id_pinjam = input("Masukkan ID Peminjam yang dikembalikan: ").strip()
    for p in daftar_peminjam:
        if p.id_peminjam == id_pinjam:
            hari_pinjam = datetime.datetime.strptime(p.tgl_pinjam, "%Y-%m-%d").date()
            hari_kembali = datetime.date.today()
            selisih = (hari_kembali - hari_pinjam).days
            denda = 0
            if selisih > 7:
                denda = (selisih - 7) * 1000 

            print("\n--- Pengembalian ---")
            print(f"ID Peminjam : {p.id_peminjam}")
            print(f"ID Anggota  : {p.id_anggota}")
            print(f"Nama        : {p.nama}")
            print(f"Alamat      : {p.alamat}")
            print(f"No. Telepon : {p.no_telp}")
            print(f"ID Buku     : {p.id_buku}")
            print(f"Judul Buku  : {p.judul}")
            print(f"Hari pinjam : {hari_pinjam}")
            print(f"Hari kembali: {hari_kembali}")
            print(f"Lama pinjam : {selisih} hari")
            if denda:
                print(f"Denda       : Rp{denda:,}")
            else:
                print("Denda        : Rp0")
            print("-------------------\n")
            
            daftar_buku = baca_file_buku()
            for buku in daftar_buku:
                if buku.id_buku == p.id_buku:
                    buku.stok += 1
                    break
                
            path_buku = os.path.join("Buku", "buku.txt")
            with open(path_buku, "w") as file:
                for b in daftar_buku:
                    if isinstance(b, BukuFiksi):
                        file.write(f"fiksi,{b.id_buku},{b.judul},{b.penulis},{b.tahun_terbit},{b.genre},{b.stok}\n")
                    else:
                        file.write(f"nonfiksi,{b.id_buku},{b.judul},{b.penulis},{b.tahun_terbit},{b.kategori},{b.stok}\n")

            daftar_peminjam.remove(p)
            path_pinjam = os.path.join(os.path.dirname(__file__), "peminjam.txt")
            with open(path_pinjam, "w") as file:
                for x in daftar_peminjam:
                    file.write(f"{x.id_peminjam},{x.id_anggota},{x.nama},{x.alamat},{x.no_telp},{x.tgl_daftar},{x.id_buku},{x.judul},{x.penulis},{x.tahun_terbit},{x.stok},{x.tgl_pinjam},{x.tgl_kembali}\n")

            print("Pengembalian berhasil diproses.\n")
            return

    print("ID Peminjam tidak ditemukan.\n")
