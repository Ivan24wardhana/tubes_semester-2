from Buku.buku import Buku, BukuFiksi, BukuNonFiksi, tampilkan_daftar_buku, baca_file_buku
from Buku.edit_buku import edit_buku
from Buku.hapus_buku import hapus_buku
from Buku.tambah_buku import tambah_buku

from Anggota.anggota import Anggota, tampilkan_daftar_anggota, baca_file_anggota
from Anggota.tambah_anggota import tambah_anggota
from Anggota.edit_anggota import edit_anggota
from Anggota.hapus_anggota import hapus_anggota

from Peminjam.peminjam import Peminjam, tampilkan_daftar_peminjam, baca_file_peminjam 
from Peminjam.tambah_peminjam import tambah_peminjam
from Peminjam.edit_peminjam import edit_peminjam
from Peminjam.kembali_peminjam import kembali_peminjam

import os

def garis():
    print("=" * 40)

def data_anggota():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        garis()
        print("       MENU DATA ANGGOTA")
        garis()
        print("1. Tambah Anggota")
        print("2. Edit Anggota")
        print("3. Hapus Anggota")
        print("4. Tampilkan Daftar Anggota")
        print("5. Kembali ke Menu Utama")
        garis()
        pilihan = input("Pilih Menu (1-5): ")

        if pilihan == "1":
            tambah_anggota()
        elif pilihan == "2":
            edit_anggota()
        elif pilihan == "3":
            hapus_anggota()
        elif pilihan == "4":
            tampilkan_daftar_anggota()
            input("\nTekan Enter untuk kembali ke menu anggota...")
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid! Coba lagi.")
            input("Tekan Enter untuk lanjut...")

def data_buku():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        garis()
        print("         MENU DATA BUKU")
        garis()
        print("1. Tambah Buku")
        print("2. Edit Buku")
        print("3. Hapus Buku")
        print("4. Tampilkan Daftar Buku")
        print("5. Kembali ke Menu Utama")
        garis()
        pilihan = input("Pilih Menu (1-5): ")

        if pilihan == "1":
            tambah_buku()
        elif pilihan == "2":
            edit_buku()
        elif pilihan == "3":
            hapus_buku()
        elif pilihan == "4":
            tampilkan_daftar_buku()
            input("\nTekan Enter untuk kembali ke menu buku...")
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid! Coba lagi.")
            input("Tekan Enter untuk lanjut...")

def data_peminjam():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        garis()
        print("       MENU DATA PEMINJAM")
        garis()
        print("1. Tambah Peminjam")
        print("2. Edit Peminjam")
        print("3. Kembali (Pengembalian Buku)")
        print("4. Tampilkan Daftar Peminjam")
        print("5. Kembali ke Menu Utama")
        garis()
        pilihan = input("Pilih Menu (1-5): ")

        if pilihan == "1":
            tambah_peminjam()
        elif pilihan == "2":
            edit_peminjam()
        elif pilihan == "3":
            kembali_peminjam()
            input("\nTekan Enter untuk kembali ke menu peminjam...")
        elif pilihan == "4":
            tampilkan_daftar_peminjam()
            input("\nTekan Enter untuk kembali ke menu peminjam...")
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid! Coba lagi.")
            input("Tekan Enter untuk lanjut...")

def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        garis()
        print("    SISTEM MANAJEMEN PERPUSTAKAAN")
        garis()
        print("1. Kelola Data Anggota")
        print("2. Kelola Data Buku")
        print("3. Kelola Data Peminjam")
        print("4. Keluar")
        garis()
        pilihan = input("Pilih Menu (1-4): ")

        if pilihan == "1":
            data_anggota()
        elif pilihan == "2":
            data_buku()
        elif pilihan == "3":
            data_peminjam()
        elif pilihan == "4":
            print("\nTerima Kasih telah menggunakan sistem!")
            break
        else:
            print("Input tidak valid! Masukkan angka 1 - 4.")
            input("Tekan Enter untuk lanjut...")

if __name__ == "__main__":
    main()
