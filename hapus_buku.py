from Buku.buku import baca_file_buku, BukuFiksi, BukuNonFiksi  # tambahkan ini

def hapus_buku():
    daftar_buku = baca_file_buku()

    if not daftar_buku:
        print("Belum ada buku yang bisa dihapus.")
        input("Tekan Enter untuk kembali...")
        return

    id_buku = input("Masukkan ID Buku yang ingin dihapus: ")

    for buku in daftar_buku:
        if buku.id_buku == id_buku:
            daftar_buku.remove(buku)

            with open("Buku/buku.txt", "w") as file:
                for b in daftar_buku:
                    if isinstance(b, BukuFiksi):
                        file.write(f"fiksi,{b.id_buku},{b.judul},{b.penulis},{b.tahun_terbit},{b.genre},{b.stok}\n")
                    elif isinstance(b, BukuNonFiksi):
                        file.write(f"nonfiksi,{b.id_buku},{b.judul},{b.penulis},{b.tahun_terbit},{b.kategori},{b.stok}\n")

            print(f"Buku dengan ID {id_buku} berhasil dihapus!\n")
            input("Tekan Enter untuk kembali...")
            return

    print(f"Buku dengan ID `{id_buku}` tidak ditemukan.")
    lanjut_hapus = input("Apakah ingin coba lagi? (y/n): ").lower()
    if lanjut_hapus == "y":
        hapus_buku()
    elif lanjut_hapus == "n":
        input("Tekan Enter untuk kembali...")
    else :
        print("Pilihan tidak valid. Kembali ke menu utama.")
        input("Tekan Enter untuk kembali...")
        return
