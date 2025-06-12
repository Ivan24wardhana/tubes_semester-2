from Anggota.anggota import baca_file_anggota


def hapus_anggota():
    daftar_anggota = baca_file_anggota()
    
    if not daftar_anggota:
        print("Belum ada anggota yang bisa dihapus.")
        input("Tekan Enter untuk kembali...")
        return

    id_anggota = input("Masukkan ID Anggota yang ingin dihapus: ")
    
    for anggota in daftar_anggota:
        if anggota.id_anggota == id_anggota:
            daftar_anggota.remove(anggota)

            with open("Anggota/anggota.txt", "w") as file:
                for a in daftar_anggota:
                    file.write(f"{a.id_anggota},{a.nama},{a.alamat},{a.no_telp},{a.tgl_daftar}\n")

            print(f"Anggota dengan ID {id_anggota} berhasil dihapus!\n")
            input("Tekan Enter untuk kembali...")
            return
        
    print(f"Anggota dengan ID `{id_anggota}` tidak ditemukan.")
    lanjut_hapus = input("Apakah ingin coba lagi? (y/n): ").lower()
    if lanjut_hapus == "y":
        hapus_anggota()
    elif lanjut_hapus == "n":
        input("Tekan Enter untuk kembali...")
    else :
        print("Pilihan tidak valid. Kembali ke menu utama.")
        input("Tekan Enter untuk kembali...")
        return



