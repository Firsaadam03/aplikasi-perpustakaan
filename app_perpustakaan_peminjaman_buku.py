# ========== Aplikasi Perpustakaan Peminjaman Buku ==========


# Data Buku
# List berisi semua data buku yang tersedia di perpustakaan
list_buku = [
    {
        "id": 1,
        "judul": "Laskar Pelangi",
        "penulis": "Andrea Hirata",
        "tahun": 2005,
        "stok": 10,
    },
    {
        "id": 2,
        "judul": "Animal Farm",
        "penulis": "George Orwell",
        "tahun": 1945,
        "stok": 10,
    },
    {
        "id": 3,
        "judul": "1984",
        "penulis": "George Orwell",
        "tahun": 1949,
        "stok": 10,
    },
    {
        "id": 4,
        "judul": "Madilog",
        "penulis": "Tan Malaka",
        "tahun": 1947,
        "stok": 10,
    },
    {
        "id": 5,
        "judul": "Sapiens",
        "penulis": "Yuval Noah Harari",
        "tahun": 2011,
        "stok": 10,
    },
]

# Counter untuk ID buku berikutnya yang akan ditambahkan
id_buku_next = 6


# Data Anggota
# List berisi semua data anggota yang terdaftar di perpustakaan
list_anggota = [
    {
        "id_anggota": 1,
        "nama": "Jokowi",
        "alamat": "Rawa Buntu",
        "no_telp": "081234567890",
    },
    {
        "id_anggota": 2,
        "nama": "Prabowo",
        "alamat": "Cisauk",
        "no_telp": "081234567891",
    },
    {
        "id_anggota": 3,
        "nama": "Ronaldo",
        "alamat": "Cisauk",
        "no_telp": "081234567892",
    },
    {
        "id_anggota": 4,
        "nama": "Messi",
        "alamat": "Cisadane",
        "no_telp": "081234567893",
    },
    {
        "id_anggota": 5,
        "nama": "Neymar",
        "alamat": "Cisadane",
        "no_telp": "081234567894",
    },
]

# Counter untuk ID anggota berikutnya yang akan ditambahkan
id_anggota_next = 6


# Data Peminjaman
# List berisi catatan semua buku yang sedang dipinjam oleh anggota
list_peminjam = [
    {
        "id_anggota": 1,
        "nama": "Jokowi",
        "id_buku": 2,
        "judul_buku": "Animal Farm",
    },
    {
        "id_anggota": 2,
        "nama": "Prabowo",
        "id_buku": 3,
        "judul_buku": "1984",
    },
    {
        "id_anggota": 3,
        "nama": "Ronaldo",
        "id_buku": 1,
        "judul_buku": "Laskar Pelangi",
    },
    {
        "id_anggota": 4,
        "nama": "Messi",
        "id_buku": 4,
        "judul_buku": "Madilog",
    },
    {
        "id_anggota": 5,
        "nama": "Neymar",
        "id_buku": 5,
        "judul_buku": "Sapiens",
    },
]

# Kurangi stok buku sesuai data peminjaman awal agar stok langsung sinkron saat program dijalankan
for p in list_peminjam:
    for b in list_buku:
        if b["id"] == p["id_buku"]:
            b["stok"] -= 1
            break


# Menu Utama
# Menampilkan pilihan menu yang tersedia kepada pengguna
def tampilkan_menu():
    print("\n=== MENU UTAMA ===")
    print("1.  Tampilkan Semua Buku")
    print("2.  Cari Buku")
    print("3.  Pinjam Buku")
    print("4.  Kembalikan Buku")
    print("5.  Tambah Buku")
    print("6.  Update Data Buku")
    print("7.  Hapus Buku")
    print("8.  Tampilkan Semua Anggota")
    print("9.  Tambah Anggota")
    print("10. Update Anggota")
    print("11. Hapus Anggota")
    print("12. Keluar Program")


# Fungsi Tampilkan Semua Buku
# Menampilkan seluruh data buku beserta status ketersediaannya
def tampilkan_semua_buku():
    if not list_buku:
        print("Belum ada data buku.")
        return
    print(
        f"\n{'ID':<5} {'Judul':<25} {'Penulis':<20} {'Tahun':<8} {'Stok':<6} {'Status'}"
    )
    print("-" * 80)
    for b in list_buku:
        status = "Tersedia" if b["stok"] > 0 else "Habis Dipinjam"
        print(
            f"{b['id']:<5} {b['judul']:<25} {b['penulis']:<20} {b['tahun']:<8} {b['stok']:<6} {status}"
        )


# Fungsi Cari Buku
# Mencari buku berdasarkan kata kunci yang dimasukkan pengguna
def cari_buku():
    kata = input("Masukkan kata kunci judul: ").lower()
    hasil = [b for b in list_buku if kata in b["judul"].lower()]
    if not hasil:
        print("! Tidak ada buku yang cocok.")
    else:
        print(
            f"\n{'ID':<5} {'Judul':<25} {'Penulis':<20} {'Tahun':<8} {'Stok':<6} {'Status'}"
        )
        print("-" * 80)
        for b in hasil:
            status = "Tersedia" if b["stok"] > 0 else "Habis Dipinjam"
            print(
                f"{b['id']:<5} {b['judul']:<25} {b['penulis']:<20} {b['tahun']:<8} {b['stok']:<6} {status}"
            )


# Fungsi Pinjam Buku
# Memproses transaksi peminjaman buku oleh anggota
def pinjam_buku():
    # Validasi ID anggota
    try:
        id_anggota = int(input("Masukkan ID anggota yang ingin meminjam: "))
    except ValueError:
        print("! ID harus berupa angka!")
        return

    anggota = next((a for a in list_anggota if a["id_anggota"] == id_anggota), None)
    if not anggota:
        print("! ID anggota tidak ditemukan.")
        return

    # Validasi ID buku
    try:
        id_buku = int(input("Masukkan ID buku yang ingin dipinjam: "))
    except ValueError:
        print("! ID harus berupa angka!")
        return

    buku = next((b for b in list_buku if b["id"] == id_buku), None)
    if not buku:
        print("! ID buku tidak ditemukan.")
        return

    # Cek ketersediaan stok buku
    if buku["stok"] <= 0:
        print(
            f"! Maaf, stok buku '{buku['judul']}' telah HABIS DIPINJAM. Silakan coba lagi nanti."
        )
        return

    # Cek apakah anggota sudah meminjam buku yang sama sebelumnya
    sudah_pinjam = any(
        p["id_anggota"] == id_anggota and p["id_buku"] == id_buku for p in list_peminjam
    )
    if sudah_pinjam:
        print(f"! Anggota '{anggota['nama']}' sudah meminjam buku ini.")
        return

    # Kurangi stok dan tambahkan ke data peminjaman
    buku["stok"] -= 1
    list_peminjam.append(
        {
            "id_anggota": id_anggota,
            "nama": anggota["nama"],
            "id_buku": id_buku,
            "judul_buku": buku["judul"],
        }
    )

    print(f"Buku '{buku['judul']}' berhasil dipinjam oleh {anggota['nama']}.")
    if buku["stok"] == 0:
        print(f"  ⚠  Perhatian: Stok buku '{buku['judul']}' kini HABIS.")
    else:
        print(f"  Stok tersisa: {buku['stok']} eksemplar.")


# Fungsi Kembalikan Buku
# Memproses pengembalian buku dari anggota dan menambahkan kembali stok
def kembalikan_buku():
    # Validasi ID anggota
    try:
        id_anggota = int(input("Masukkan ID anggota yang mengembalikan: "))
    except ValueError:
        print("! ID harus berupa angka!")
        return

    anggota = next((a for a in list_anggota if a["id_anggota"] == id_anggota), None)
    if not anggota:
        print("! ID anggota tidak ditemukan.")
        return

    # Validasi ID buku
    try:
        id_buku = int(input("Masukkan ID buku yang dikembalikan: "))
    except ValueError:
        print("! ID harus berupa angka!")
        return

    # Cari record peminjaman yang sesuai
    record = next(
        (
            p
            for p in list_peminjam
            if p["id_anggota"] == id_anggota and p["id_buku"] == id_buku
        ),
        None,
    )
    if not record:
        print("! Tidak ditemukan data peminjaman untuk anggota dan buku tersebut.")
        return

    # Tambahkan stok kembali dan hapus record peminjaman
    buku = next((b for b in list_buku if b["id"] == id_buku), None)
    if buku:
        buku["stok"] += 1

    list_peminjam.remove(record)
    judul = buku["judul"] if buku else f"ID {id_buku}"
    print(f"Buku '{judul}' berhasil dikembalikan oleh {anggota['nama']}.")
    if buku:
        print(f"  Stok sekarang: {buku['stok']} eksemplar.")


# Fungsi Tambah Buku
# Menambahkan data buku baru ke dalam list_buku
def tambah_buku():
    global id_buku_next
    judul = input("Judul buku: ").strip()
    penulis = input("Penulis buku: ").strip()

    # Validasi input tahun
    try:
        tahun = int(input("Tahun terbit: "))
    except ValueError:
        print("! Tahun harus berupa angka!")
        return
    if not (1900 <= tahun <= 2025):
        print("! Tahun harus antara 1900–2025!")
        return

    # Validasi input stok
    try:
        stok = int(input("Jumlah stok: "))
        if stok < 1:
            print("! Stok minimal 1!")
            return
    except ValueError:
        print("! Stok harus berupa angka!")
        return

    # Cek apakah judul buku sudah ada sebelumnya
    for b in list_buku:
        if b["judul"].lower() == judul.lower():
            print("! Buku dengan judul ini sudah ada!")
            return

    # Konfirmasi dan simpan data buku baru
    konfirmasi = input("Apakah yakin ingin menyimpan? (y/n): ")
    if konfirmasi.lower() == "y":
        list_buku.append(
            {
                "id": id_buku_next,
                "judul": judul,
                "penulis": penulis,
                "tahun": tahun,
                "stok": stok,
            }
        )
        print(f"Buku dengan ID {id_buku_next} berhasil ditambahkan.")
        id_buku_next += 1
    else:
        print("! Penambahan dibatalkan.")


# Fungsi Update Data Buku
# Mengubah data buku yang sudah ada berdasarkan ID buku
def update_buku():
    try:
        id_buku = int(input("Masukkan ID buku yang ingin diupdate: "))
    except ValueError:
        print("! ID harus berupa angka!")
        return

    for b in list_buku:
        if b["id"] == id_buku:
            print(f"Data lama: {b}")

            judul = input("Judul baru: ").strip()
            penulis = input("Penulis baru: ").strip()

            # Validasi tahun baru
            try:
                tahun = int(input("Tahun baru: "))
            except ValueError:
                print("! Tahun harus berupa angka!")
                return
            if not (1900 <= tahun <= 2025):
                print("! Tahun harus antara 1900–2025!")
                return

            # Validasi stok baru
            try:
                stok = int(input("Stok baru: "))
                if stok < 0:
                    print("! Stok tidak boleh negatif!")
                    return
            except ValueError:
                print("! Stok harus berupa angka!")
                return

            # Konfirmasi dan terapkan perubahan
            konfirmasi = input("Apakah yakin ingin mengupdate data ini? (y/n): ")
            if konfirmasi.lower() == "y":
                b.update(
                    {"judul": judul, "penulis": penulis, "tahun": tahun, "stok": stok}
                )
                print("Data berhasil diupdate.")
            else:
                print("! Perubahan dibatalkan.")
            return

    print("! ID buku tidak ditemukan.")


# Fungsi Hapus Buku
# Menghapus data buku dari list_buku berdasarkan ID (hanya jika tidak sedang dipinjam)
def hapus_buku():
    try:
        id_buku = int(input("Masukkan ID buku yang ingin dihapus: "))
    except ValueError:
        print("! ID harus berupa angka!")
        return

    for b in list_buku:
        if b["id"] == id_buku:
            # Cek apakah buku masih ada dalam daftar peminjaman aktif
            sedang_dipinjam = any(p["id_buku"] == id_buku for p in list_peminjam)
            if sedang_dipinjam:
                print("! Buku ini masih dipinjam, tidak bisa dihapus.")
                return

            print(f"Data: {b}")
            konfirmasi = input("Apakah yakin ingin menghapus data ini? (y/n): ")
            if konfirmasi.lower() == "y":
                list_buku.remove(b)
                print("Data berhasil dihapus.")
            else:
                print("! Penghapusan dibatalkan.")
            return

    print("! ID buku tidak ditemukan.")


# Fungsi Tampilkan Semua Anggota
# Menampilkan seluruh data anggota beserta buku yang sedang dipinjam
def tampilkan_semua_anggota():
    if not list_anggota:
        print("Belum ada data anggota.")
        return
    print(f"\n{'ID':<6} {'Nama':<15} {'Alamat':<15} {'No. Telp':<15} {'Buku Dipinjam'}")
    print("-" * 70)
    for a in list_anggota:
        pinjaman = [
            p["judul_buku"] for p in list_peminjam if p["id_anggota"] == a["id_anggota"]
        ]
        buku_info = ", ".join(pinjaman) if pinjaman else "-"
        print(
            f"{a['id_anggota']:<6} {a['nama']:<15} {a['alamat']:<15} {a['no_telp']:<15} {buku_info}"
        )


# Fungsi Tambah Anggota
# Menambahkan data anggota baru ke dalam list_anggota
def tambah_anggota():
    global id_anggota_next
    nama = input("Nama anggota: ").strip()
    if not nama:
        print("! Nama tidak boleh kosong!")
        return

    alamat = input("Alamat: ").strip()
    no_telp = input("No. Telepon: ").strip()

    # Cek apakah nama anggota sudah terdaftar sebelumnya
    for a in list_anggota:
        if a["nama"].lower() == nama.lower():
            print("! Anggota dengan nama ini sudah terdaftar!")
            return

    # Konfirmasi dan simpan data anggota baru
    konfirmasi = input("Apakah yakin ingin menyimpan? (y/n): ")
    if konfirmasi.lower() == "y":
        list_anggota.append(
            {
                "id_anggota": id_anggota_next,
                "nama": nama,
                "alamat": alamat,
                "no_telp": no_telp,
            }
        )
        print(f"Anggota '{nama}' berhasil ditambahkan dengan ID {id_anggota_next}.")
        id_anggota_next += 1
    else:
        print("! Penambahan dibatalkan.")


# Fungsi Update Anggota
# Mengubah data anggota yang sudah ada berdasarkan ID anggota
def update_anggota():
    try:
        id_anggota = int(input("Masukkan ID anggota yang ingin diupdate: "))
    except ValueError:
        print("! ID harus berupa angka!")
        return

    anggota = next((a for a in list_anggota if a["id_anggota"] == id_anggota), None)
    if not anggota:
        print("! ID anggota tidak ditemukan.")
        return

    print(f"Data lama: {anggota}")
    nama = input("Nama baru: ").strip()
    if not nama:
        print("! Nama tidak boleh kosong!")
        return

    alamat = input("Alamat baru: ").strip()
    no_telp = input("No. Telepon baru: ").strip()

    # Cek apakah nama baru sudah dipakai anggota lain
    for a in list_anggota:
        if a["nama"].lower() == nama.lower() and a["id_anggota"] != id_anggota:
            print("! Nama ini sudah digunakan anggota lain!")
            return

    # Konfirmasi dan terapkan perubahan
    konfirmasi = input("Apakah yakin ingin mengupdate data ini? (y/n): ")
    if konfirmasi.lower() == "y":
        anggota.update({"nama": nama, "alamat": alamat, "no_telp": no_telp})
        # Sinkronkan nama di data peminjaman yang aktif
        for p in list_peminjam:
            if p["id_anggota"] == id_anggota:
                p["nama"] = nama
        print(f"Data anggota '{nama}' berhasil diupdate.")
    else:
        print("! Perubahan dibatalkan.")


# Fungsi Hapus Anggota
# Menghapus data anggota dari list_anggota (hanya jika tidak ada buku yang masih dipinjam)
def hapus_anggota():
    try:
        id_anggota = int(input("Masukkan ID anggota yang ingin dihapus: "))
    except ValueError:
        print("! ID harus berupa angka!")
        return

    anggota = next((a for a in list_anggota if a["id_anggota"] == id_anggota), None)
    if not anggota:
        print("! ID anggota tidak ditemukan.")
        return

    # Cek apakah anggota masih memiliki buku yang belum dikembalikan
    masih_pinjam = any(p["id_anggota"] == id_anggota for p in list_peminjam)
    if masih_pinjam:
        buku_pinjaman = [
            p["judul_buku"] for p in list_peminjam if p["id_anggota"] == id_anggota
        ]
        print(
            f"! Anggota '{anggota['nama']}' masih meminjam buku: {', '.join(buku_pinjaman)}."
        )
        print("  Kembalikan buku terlebih dahulu sebelum menghapus anggota.")
        return

    print(f"Data: {anggota}")
    konfirmasi = input("Apakah yakin ingin menghapus anggota ini? (y/n): ")
    if konfirmasi.lower() == "y":
        list_anggota.remove(anggota)
        print(f"Anggota '{anggota['nama']}' berhasil dihapus.")
    else:
        print("! Penghapusan dibatalkan.")


# Main Loop
# Perulangan utama program yang terus berjalan sampai pengguna memilih keluar
while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-12): ").strip()

    if pilihan == "1":
        tampilkan_semua_buku()
    elif pilihan == "2":
        cari_buku()
    elif pilihan == "3":
        pinjam_buku()
    elif pilihan == "4":
        kembalikan_buku()
    elif pilihan == "5":
        tambah_buku()
    elif pilihan == "6":
        update_buku()
    elif pilihan == "7":
        hapus_buku()
    elif pilihan == "8":
        tampilkan_semua_anggota()
    elif pilihan == "9":
        tambah_anggota()
    elif pilihan == "10":
        update_anggota()
    elif pilihan == "11":
        hapus_anggota()
    elif pilihan == "12":
        print("Terima kasih telah menggunakan program.")
        break
    else:
        print("! Pilihan tidak valid, coba lagi.")
