from Anggota.anggota import Anggota, baca_file_anggota
import datetime
import os

def edit_anggota():
    daftar_anggota = baca_file_anggota()
    
    if not daftar_anggota:
        print("Belum ada anggota yang bisa diedit.")
        input("Tekan Enter untuk kembali...")
        return

    id_anggota = input("Masukkan ID Anggota yang ingin diedit: ")

    for anggota in daftar_anggota:
        if anggota.id_anggota == id_anggota:
            print("\nData lama:")
            anggota.tampilkan_anggota()
            print()

            anggota.id_anggota  = input("Masukkan ID Anggota Baru  (kosongkan jika tidak ingin mengubah)        : ") or anggota.id_anggota
            anggota.nama        = input("Masukkan Nama Baru        (kosongkan jika tidak ingin mengubah)        : ") or anggota.nama
            anggota.alamat      = input("Masukkan Alamat Baru      (kosongkan jika tidak ingin mengubah)        : ") or anggota.alamat
            anggota.no_telp     = input("Masukkan No Telp Baru     (kosongkan jika tidak ingin mengubah)        : ") or anggota.no_telp

            path_file = os.path.join(os.path.dirname(__file__), "anggota.txt")
            with open(path_file, "w") as file:
                for a in daftar_anggota:
                    file.write(f"{a.id_anggota},{a.nama},{a.alamat},{a.no_telp},{a.tgl_daftar}\n")

            print("Data Anggota berhasil diperbarui.\n")
            lanjut_edit = input("Apakah ingin lanjut edit Anggota lain? (y/n): ").lower()
            if lanjut_edit == "y":
                edit_anggota()
            else:
                input("Tekan Enter untuk kembali...")
            return

    print(f"Anggota dengan ID `{id_anggota}` tidak ditemukan.")
    lanjut_edit = input("Apakah ingin coba lagi? (y/n): ").lower()
    if lanjut_edit == "y":
        edit_anggota()
    else:
        input("Tekan Enter untuk kembali...")
    return