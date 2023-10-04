__author__ = "rizkyhaksono"
__copyright__ = "Copyright 2023, Malang"

# Fungsi untuk menghitung nilai akhir


def hitung_nilai_akhir(uts, uas):
    return (uts + uas) / 2

# Fungsi untuk menghitung semua nilai akhir


def hitung_semua_nilai_akhir(data_mahasiswa):
    data_nilai_akhir = {}
    for nama, nilai in data_mahasiswa.items():
        nilai_akhir = hitung_nilai_akhir(nilai['uts'], nilai['uas'])
        data_nilai_akhir[nama] = nilai_akhir
    return data_nilai_akhir

# Fungsi untuk menampilkan hasil nilai akhir


def tampilkan_nilai_akhir(data_nilai_akhir):
    print("Hasil Nilai Akhir Mahasiswa:")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print("Nama: {}\tNilai Akhir: {:.2f}".format(nama, nilai_akhir))

# Program utama


def main():
    data_mahasiswa = {
        'Rizky': {'uts': 80, 'uas': 85},
        'Haksono': {'uts': 75, 'uas': 90},
        'Natee': {'uts': 90, 'uas': 10},
    }

    # hitung dulu lalu masuk ke data_nilai_akhir
    data_nilai_akhir = hitung_semua_nilai_akhir(data_mahasiswa)

    # panggil function
    tampilkan_nilai_akhir(data_nilai_akhir)


# main
if __name__ == "__main__":
    main()
