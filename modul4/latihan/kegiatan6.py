__author__ = "rizkyhaksono"
__copyright__ = "Copyright 2023, Malang"


# Percobaan 6
def point(x, y):
    return x, y


def line_equation_of(x1, y1, M):
    C = y1 - M * x1
    return f"y = {M:.2f}x + {C:.2f}"


# Ubah nilai input dengan 3 digit NIM akhir 189
print("Persamaan garis yang melalui titik (3,2) dan bergradien 5:")
print(line_equation_of(3, 2, 5))
