from Peminjam.peminjam import Peminjam, baca_file_peminjam
from Anggota.anggota import Anggota
from Buku.buku import Buku
import datetime
import os

def edit_peminjam():
    daftar_peminjam = baca_file_peminjam()

    if not daftar_peminjam:
        print("Belum ada data peminjam yang bisa diedit.")
        input("Tekan Enter untuk kembali...")
        return

    id_peminjam = input("Masukkan ID Peminjam yang ingin diedit: ")

    for peminjam in daftar_peminjam:
        if peminjam.id_peminjam == id_peminjam:
            print("\nData lama:")
            peminjam.tampilkan_peminjam()
            print()

            id_anggota_baru = input("Masukkan ID Anggota Baru (kosongkan jika tidak ingin mengubah): ")
            id_buku_baru = input("Masukkan ID Buku Baru    (kosongkan jika tidak ingin mengubah): ")
            ubah_tgl_pinjam = input("Pilih y/n untuk mengubah tanggal pinjam (y/n): ").lower()

            if ubah_tgl_pinjam == 'y':
                peminjam.tgl_pinjam = datetime.date.today()

            # Update anggota
            if id_anggota_baru:
                try:
                    with open(os.path.join("Anggota", "anggota.txt"), "r") as file:
                        for line in file:
                            data = line.strip().split(",")
                            if data[0].strip() == id_anggota_baru:
                                anggota_baru = Anggota(data[0], data[1], data[2], data[3], data[4])
                                peminjam.id_anggota = anggota_baru.id_anggota
                                peminjam.nama = anggota_baru.nama
                                peminjam.alamat = anggota_baru.alamat
                                peminjam.no_telp = anggota_baru.no_telp
                                peminjam.tgl_daftar = anggota_baru.tgl_daftar
                                break
                        else:
                            print("ID Anggota tidak ditemukan.")
                            input("Tekan Enter untuk kembali...")
                            return
                except FileNotFoundError:
                    print("File anggota.txt tidak ditemukan.")
                    return

            # Update buku
            if id_buku_baru:
                try:
                    with open(os.path.join("Buku", "buku.txt"), "r") as file:
                        for line in file:
                            data = line.strip().split(",")
                            if data[1].strip() == id_buku_baru:
                                buku_baru = Buku(data[1], data[2], data[3], data[4])
                                peminjam.id_buku = buku_baru.id_buku
                                peminjam.judul = buku_baru.judul
                                peminjam.penulis = buku_baru.penulis
                                peminjam.tahun_terbit = buku_baru.tahun_terbit
                                peminjam.stok = buku_baru.stok
                                break
                        else:
                            print("ID Buku tidak ditemukan.")
                            input("Tekan Enter untuk kembali...")
                            return
                except FileNotFoundError:
                    print("File buku.txt tidak ditemukan.")
                    return

            # Simpan perubahan
            path_file = os.path.join(os.path.dirname(__file__), "peminjam.txt")
            with open(path_file, "w") as file:
                for p in daftar_peminjam:
                    file.write(f"{p.id_peminjam},{p.id_anggota},{p.nama},{p.alamat},{p.no_telp},{p.id_buku},{p.judul},{p.penulis},{p.tahun_terbit},{p.tgl_pinjam},{p.tgl_kembali}\n")

            print("Data peminjam berhasil diperbarui!\n")
            input("Tekan Enter untuk kembali...")
            return

    # Jika tidak ditemukan
    print(f"Peminjam dengan ID `{id_peminjam}` tidak ditemukan.")
    lanjut = input("Apakah ingin coba lagi? (y/n): ").lower()
    if lanjut == "y":
        edit_peminjam()
    else:
        input("Tekan Enter untuk kembali...")
