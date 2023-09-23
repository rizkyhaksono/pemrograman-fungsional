__author__      = "rizkyhaksono"
__copyright__   = "Copyright 2023, Malang"

# Sistem penilaian mahasiswa

# Tambahkan fungsi untuk menghitung nilai akhir

# Tambahkan fungsi untuk menghitung semua nilai akhir

# Fungsi untuk menampilkan hasil nilai akhir
def tampilkan_nilai_akhir(data_nilai_akhir):
    print("Hasil Nilai Akhir Mahasiswa:")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print("Nama: {}\tNilai Akhir: {:.2f}".format(nama, nilai_akhir))


# Program utama
def main():
    data_mahasiswa = {
        # Data mahasiswa (nama sebagai kunci dan nilai UTS serta UAS sebagai nilai dalam bentuk dictionary)
    }

    data_nilai_akhir =  # Menghitung nilai akhir semua mahasiswa

    tampilkan_nilai_akhir(data_nilai_akhir)

if __name__ == "__main__":
    main()