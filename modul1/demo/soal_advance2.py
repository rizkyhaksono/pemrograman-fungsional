__author__ = "rizkyhaksono"
__copyright__ = "Copyright 2023, Malang"

# Inisialisasi data buku dalam bentuk list
data_buku = []

# Inisialisasi data peminjaman buku dalam bentuk dictionary
peminjaman_buku = {}

# Fungsi untuk admin menambahkan buku


def tambah_buku():
    judul = input("Masukkan judul buku: ")
    penulis = input("Masukkan nama penulis: ")
    data_buku.append((judul, penulis))
    print("Buku berhasil ditambahkan.")

# Fungsi untuk menampilkan daftar buku yang tersedia


def tampilkan_daftar_buku():
    print("\nDaftar Buku Tersedia:")
    for i, buku in enumerate(data_buku):
        print(f"{i + 1}. Judul: {buku[0]}, Penulis: {buku[1]}")

# Fungsi untuk user melakukan peminjaman buku


def pinjam_buku(username):
    tampilkan_daftar_buku()
    pilihan = int(input("\nPilih buku yang ingin dipinjam (nomor): ")) - 1

    if 0 <= pilihan < len(data_buku):
        buku_dipinjam = data_buku[pilihan]
        if buku_dipinjam not in peminjaman_buku.values():
            peminjaman_buku[username] = buku_dipinjam
            print(
                f"Buku '{buku_dipinjam[0]}' berhasil dipinjam oleh {username}.")
        else:
            print("Buku ini sudah dipinjam oleh pengguna lain.")
    else:
        print("Nomor buku tidak valid.")

# Fungsi untuk user mengembalikan buku


def kembalikan_buku(username):
    if username in peminjaman_buku:
        buku_dikembalikan = peminjaman_buku.pop(username)
        print(
            f"Buku '{buku_dikembalikan[0]}' berhasil dikembalikan oleh {username}.")
    else:
        print("Anda tidak memiliki buku yang sedang dipinjam.")

# Fungsi untuk menampilkan menu admin


def menu_admin():
    while True:
        print("\nMenu Admin:")
        print("1. Tambah Buku")
        print("2. Kembali ke Menu Utama")

        admin_pilihan = input("Pilih menu admin (1/2): ")

        if admin_pilihan == "1":
            tambah_buku()
        elif admin_pilihan == "2":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Fungsi untuk menampilkan menu user


def menu_user(username):
    while True:
        print("\nMenu User:")
        print("1. Pinjam Buku")
        print("2. Kembalikan Buku")
        print("3. Kembali ke Menu Utama")

        user_pilihan = input("Pilih menu user (1/2/3): ")

        if user_pilihan == "1":
            pinjam_buku(username)
        elif user_pilihan == "2":
            kembalikan_buku(username)
        elif user_pilihan == "3":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Fungsi untuk menampilkan menu utama


def menu_utama():
    while True:
        print("\nMenu Utama:")
        print("1. Admin")
        print("2. User")
        print("3. Keluar")

        akun = input("Masukkan jenis akun (admin/user/keluar): ").lower()

        if akun == "admin":
            menu_admin()
        elif akun == "user":
            username = input("Masukkan nama pengguna: ")
            menu_user(username)
        elif akun == "keluar":
            break
        else:
            print("Akun tidak valid. Silakan coba lagi.")


# Memanggil fungsi menu_utama untuk menjalankan program
menu_utama()
