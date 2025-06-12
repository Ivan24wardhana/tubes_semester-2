from Buku.buku import Buku, BukuFiksi, BukuNonFiksi, baca_file_buku
import os

def edit_buku():
    daftar_buku = baca_file_buku()

    if not daftar_buku:
        print("Belum ada buku yang bisa diedit.")
        input("Tekan Enter untuk kembali...")
        return

    id_buku = input("Masukkan ID Buku yang ingin diedit: ")

    for buku in daftar_buku:
        if buku.id_buku == id_buku:
            print("\nData lama:")
            buku.tampilkan_buku()

            buku.id_buku      = input("Masukkan ID Buku Baru (kosongkan jika tidak ingin mengubah)      : ") or buku.id_buku
            buku.judul        = input("Masukkan Judul Baru (kosongkan jika tidak ingin mengubah)        : ") or buku.judul
            buku.penulis      = input("Masukkan Penulis Baru (kosongkan jika tidak ingin mengubah)      : ") or buku.penulis
            buku.tahun_terbit = input("Masukkan Tahun Terbit Baru (kosongkan jika tidak ingin mengubah) : ") or buku.tahun_terbit
            buku.stok         = input("Masukkan Stok Baru (kosongkan jika tidak ingin mengubah)         : ") or buku.stok

            if isinstance(buku, BukuFiksi):
                buku.genre = input("Masukkan Genre Baru (kosongkan jika tidak ingin mengubah)        : ") or buku.genre
            elif isinstance(buku, BukuNonFiksi):
                buku.kategori = input("Masukkan Kategori Baru (kosongkan jika tidak ingin mengubah)     : ") or buku.kategori

            path_file = os.path.join(os.path.dirname(__file__), "buku.txt")
            with open(path_file, "w") as file:
                for b in daftar_buku:
                    if isinstance(b, BukuFiksi):
                        file.write(f"fiksi,{b.id_buku},{b.judul},{b.penulis},{b.tahun_terbit},{b.genre},{b.stok}\n")
                    elif isinstance(b, BukuNonFiksi):
                        file.write(f"nonfiksi,{b.id_buku},{b.judul},{b.penulis},{b.tahun_terbit},{b.kategori},{b.stok}\n")

            print("\nData buku berhasil diperbarui.")
            lanjut_edit = input("Apakah ingin lanjut edit buku lain? (y/n): ").lower()
            if lanjut_edit == "y":
                edit_buku()
            else:
                input("Tekan Enter untuk kembali...")
            return

    print(f"Buku dengan ID `{id_buku}` tidak ditemukan.")
    lanjut_edit = input("Apakah ingin coba lagi? (y/n): ").lower()
    if lanjut_edit == "y":
        edit_buku()
    else:
        input("Tekan Enter untuk kembali...")
