__author__ = "rizkyhaksono"
__copyright__ = "Copyright 2023, Malang"

import math


def translasi(x, y):
    def inner(tx, ty):
        new_x = x + tx
        new_y = y + ty
        return new_x, new_y

    return inner


def dilatasi(x, y):
    def inner(sx, sy):
        new_x = x * sx
        new_y = y * sy
        return new_x, new_y

    return inner


def float_output(function):
    def inner(*args, **kwargs):
        result = function(*args, **kwargs)
        return f"{result[0]:.5f}, {result[1]:.5f}"

    return inner


@float_output
def rotasi(x, y, sudut):
    radian = math.radians(sudut)
    new_x = x * math.cos(radian) - y * math.sin(radian)
    new_y = x * math.sin(radian) + y * math.cos(radian)
    return new_x, new_y


# Titik awal
titik_P = (3, 5)

# Translasi
titik_setelah_translasi = translasi(*titik_P)(2, -1)
print("Koordinat setelah translasi:", titik_setelah_translasi)

# Dilatasi
titik_setelah_dilatasi = dilatasi(*titik_P)(2, -1)
print("Koordinat setelah dilatasi:", titik_setelah_dilatasi)

# Rotasi
titik_setelah_rotasi = rotasi(*titik_P, 30)
print("Koordinat setelah rotasi:", titik_setelah_rotasi)
