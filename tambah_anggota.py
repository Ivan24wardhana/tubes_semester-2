from Anggota.anggota import Anggota, baca_file_anggota
import datetime
import os

def tambah_anggota():
    id_anggota = input("Masukkan ID Anggota             : ")
    nama       = input("Masukkan Nama Anggota           : ")
    alamat     = input("Masukkan Alamat Anggota         : ")
    no_telp    = input("Masukkan No Telp Anggota        : ")
    tgl_daftar = datetime.date.today()

    anggota_baru = Anggota(id_anggota, nama, alamat, no_telp, tgl_daftar)
    simpan_anggota(anggota_baru)
    
    print("\nData anggota berhasil ditambahkan.")
    lanjut_edit = input("\nApakah ingin tambah anggota lain? (y/n): ").lower()
    if lanjut_edit == "y":
        tambah_anggota()
    else:
        input("Tekan Enter untuk kembali...")
    return

def simpan_anggota(anggota):
    path_file = os.path.join(os.path.dirname(__file__), "anggota.txt")
    with open(path_file, "a") as file:
        file.write(f"{anggota.id_anggota},{anggota.nama},{anggota.alamat},{anggota.no_telp},{anggota.tgl_daftar}\n")
        
