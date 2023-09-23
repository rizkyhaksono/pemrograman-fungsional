__author__      = "rizkyhaksono"
__copyright__   = "Copyright 2023, Malang"

# Inisialisasi data peserta dalam bentuk list
data_peserta = []

# Fungsi untuk menambahkan data peserta oleh admin
def tambah_data_peserta():
    id_peserta = len(data_peserta)  # ID akan diurutkan secara otomatis
    nama = input("Masukkan nama peserta: ")
    nilai = float(input("Masukkan nilai peserta: "))
    hasil_akhir = "Lolos" if nilai >= 75 else "Tidak Lolos"
    data_peserta.append((id_peserta, nama, nilai, hasil_akhir))
    print("Data peserta berhasil ditambahkan.")

# Fungsi untuk mengedit nilai peserta oleh admin
def edit_nilai_peserta():
    id_peserta = int(input("Masukkan ID peserta yang ingin diedit nilainya: "))
    if 0 <= id_peserta < len(data_peserta):
        nilai_baru = float(input("Masukkan nilai baru peserta: "))
        hasil_akhir_baru = "Lolos" if nilai_baru >= 75 else "Tidak Lolos"
        data_peserta[id_peserta] = (data_peserta[id_peserta][0], data_peserta[id_peserta][1], nilai_baru, hasil_akhir_baru)
        print("Nilai peserta berhasil diubah.")
    else:
        print("ID peserta tidak valid.")

# Fungsi untuk peserta melihat nilai dan hasil akhirnya sendiri
def lihat_nilai_hasil_peserta(id_peserta):
    if 0 <= id_peserta < len(data_peserta):
        print(f"Nama: {data_peserta[id_peserta][1]}")
        print(f"Nilai: {data_peserta[id_peserta][2]}")
        print(f"Hasil Akhir: {data_peserta[id_peserta][3]}")
    else:
        print("ID peserta tidak valid.")

# Program utama
while True:
    print("\nMenu:")
    print("1. Tambah Data Peserta (Admin)")
    print("2. Edit Nilai Peserta (Admin)")
    print("3. Lihat Nilai dan Hasil Akhir (Peserta)")
    print("4. Keluar")
    
    akun = input("Masukkan jenis akun (admin/peserta): ").lower()
    
    if akun == "admin":
        print("\nMenu Admin:")
        print("1. Tambah Data Peserta")
        print("2. Edit Nilai Peserta")
        admin_pilihan = input("Pilih menu admin: ")
        if admin_pilihan == "1":
            tambah_data_peserta()
        elif admin_pilihan == "2":
            edit_nilai_peserta()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
    elif akun == "peserta":
        peserta_id = int(input("Masukkan ID peserta Anda: "))
        lihat_nilai_hasil_peserta(peserta_id)
    elif akun == "keluar":
        break
    else:
        print("Akun tidak valid. Silakan coba lagi.")
