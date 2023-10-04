__author__ = "rizkyhaksono"
__copyright__ = "Copyright 2023, Malang"

# List
data_buku = []

# Dict
peminjaman_buku = {}

# Data dummy
akun_admin = {"admin": "password123"}
akun_pengguna = {"rizky": "haksono", "user": "userpass123"}


def tambah_buku():
    judul = input("Masukkan judul buku: ")
    penulis = input("Masukkan nama penulis: ")
    data_buku.append((judul, penulis))
    print("Buku berhasil ditambahkan.")


def tampilkan_daftar_buku():
    print("\nDaftar Buku Tersedia:")
    for i, buku in enumerate(data_buku):
        # Formatted string
        print(f"{i + 1}. Judul: {buku[0]}, Penulis: {buku[1]}")


def pinjam_buku(username):
    tampilkan_daftar_buku()
    pilihan = int(input("\nPilih buku yang ingin dipinjam (nomor): ")) - 1

    if 0 <= pilihan < len(data_buku):
        buku_dipinjam = data_buku[pilihan]
        if not cek_peminjaman(buku_dipinjam):
            peminjaman_buku[username] = buku_dipinjam
            # Formatted string
            print(
                f"Buku '{buku_dipinjam[0]}' berhasil dipinjam oleh {username}.")
        else:
            print("Buku ini sudah dipinjam oleh pengguna lain.")
    else:
        print("Nomor buku tidak valid.")


def kembalikan_buku(username):
    if username in peminjaman_buku:
        buku_dikembalikan = peminjaman_buku.pop(username)
        # Formatted string
        print(
            f"Buku '{buku_dikembalikan[0]}' berhasil dikembalikan oleh {username}.")
    else:
        print("Anda tidak memiliki buku yang sedang dipinjam.")


def cek_peminjaman(buku):
    for user, peminjaman in peminjaman_buku.items():
        if peminjaman == buku:
            return True
    return False


def menu_admin():
    while True:
        print("\nMenu Admin:")
        print("1. Tambah Buku")
        print("2. Kembali ke Menu Utama")

        admin_pilihan = input("Pilih menu admin: ")

        if admin_pilihan == "1":
            tambah_buku()
        elif admin_pilihan == "2":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


def menu_user(username):
    while True:
        print("\nMenu User:")
        print("1. Pinjam Buku")
        print("2. Kembalikan Buku")
        print("3. Kembali ke Menu Utama")

        user_pilihan = input("Pilih menu user: ")

        if user_pilihan == "1":
            pinjam_buku(username)
        elif user_pilihan == "2":
            kembalikan_buku(username)
        elif user_pilihan == "3":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


def menu_utama():
    while True:
        print("\nMenu Utama:")
        print("1. Admin")
        print("2. User")
        print("3. Keluar")

        akun = input("Masukkan jenis akun: ").lower()

        if akun == "admin":
            # Validasi akun admin
            username = input("Masukkan nama pengguna: ")
            password = input("Masukkan password: ")
            if akun_admin.get(username) == password:
                menu_admin()
            else:
                print("Akun admin tidak valid.")
        elif akun == "user":
            # Validasi akun pengguna
            username = input("Masukkan nama pengguna: ")
            password = input("Masukkan password: ")
            if akun_pengguna.get(username) == password:
                menu_user(username)
            else:
                print("Akun user tidak valid.")
        elif akun == "keluar":
            break
        else:
            print("Akun tidak valid. Silakan coba lagi.")


# Main
menu_utama()
