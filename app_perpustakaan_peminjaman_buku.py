# === SISTEM PENCATATAN BUKU ===
# Program CRUD sederhana untuk mencatat data buku bacaan

buku_list = []
next_id = 1


def tampilkan_menu():
    print("\n=== MENU UTAMA ===")
    print("1. Tambah Buku")
    print("2. Tampilkan Semua Buku")
    print("3. Cari Buku")
    print("4. Ubah Data Buku")
    print("5. Hapus Buku")
    print("6. Keluar Program")


def tambah_buku():
    global next_id
    judul = input("Judul buku: ")
    penulis = input("Penulis buku: ")
    try:
        tahun = int(input("Tahun terbit: "))
    except ValueError:
        print("Tahun harus berupa angka!")
        return
    if tahun < 1900 or tahun > 2025:
        print("Tahun harus antara 1900–2025!")
        return
    buku = {"id": next_id, "judul": judul, "penulis": penulis, "tahun": tahun}
    buku_list.append(buku)
    print(f"Buku dengan ID {next_id} berhasil ditambahkan.")
    next_id += 1


def tampilkan_semua():
    if not buku_list:
        print("Belum ada data buku.")
        return
    print("\nID | Judul | Penulis | Tahun")
    print("-" * 40)
    for b in buku_list:
        print(f"{b['id']} | {b['judul']} | {b['penulis']} | {b['tahun']}")


def cari_buku():
    kata = input("Masukkan kata kunci judul: ").lower()
    hasil = []
    for b in buku_list:
        if kata in b["judul"].lower():
            hasil.append(b)
    if not hasil:
        print("Tidak ada buku yang cocok.")
    else:
        print("\nHasil pencarian:")
        for b in hasil:
            print(f"{b['id']} | {b['judul']} | {b['penulis']} | {b['tahun']}")


def ubah_buku():
    try:
        id_buku = int(input("Masukkan ID buku yang ingin diubah: "))
    except ValueError:
        print("ID harus berupa angka!")
        return
    for b in buku_list:
        if b["id"] == id_buku:
            print(f"Data lama: {b}")
            judul = input("Judul baru: ")
            penulis = input("Penulis baru: ")
            try:
                tahun = int(input("Tahun baru: "))
            except ValueError:
                print("Tahun harus berupa angka!")
                return
            if tahun < 1900 or tahun > 2025:
                print("Tahun harus antara 1900-2025!")
                return
            konfirmasi = input("Apakah yakin ingin mengubah data ini? (y/n): ")
            if konfirmasi.lower() == "y":
                b["judul"] = judul
                b["penulis"] = penulis
                b["tahun"] = tahun
                print("Data berhasil diubah.")
            else:
                print("Perubahan dibatalkan.")
            return
    print("ID buku tidak ditemukan.")


def hapus_buku():
    try:
        id_buku = int(input("Masukkan ID buku yang ingin dihapus: "))
    except ValueError:
        print("ID harus berupa angka!")
        return
    for b in buku_list:
        if b["id"] == id_buku:
            print(f"Data: {b}")
            konfirmasi = input("Apakah yakin ingin menghapus data ini? (y/n): ")
            if konfirmasi.lower() == "y":
                buku_list.remove(b)
                print("Data berhasil dihapus.")
            else:
                print("Penghapusan dibatalkan.")
            return
    print("ID buku tidak ditemukan.")


# === MAIN LOOP ===
while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-6): ")
    if pilihan == "1":
        tambah_buku()
    elif pilihan == "2":
        tampilkan_semua()
    elif pilihan == "3":
        cari_buku()
    elif pilihan == "4":
        ubah_buku()
    elif pilihan == "5":
        hapus_buku()
    elif pilihan == "6":
        print("Terima kasih telah menggunakan program.")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")
