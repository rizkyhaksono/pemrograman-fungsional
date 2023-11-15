def point(x, y):
    return x, y

def line_equation_of(p1, p2):
    #TODO 1: menggunakan inner function dan closure untuk menhitung nilai m
    def calculate_gradient(p1, p2):
        # Rumus untuk menghitung gradien (m)
        return (p2[1] - p1[1]) / (p2[0] - p1[0])

    # Mendapatkan nilai gradien
    M = calculate_gradient(p1, p2)

    # Rumus untuk menghitung konstanta (c)
    C = p1[1] - M * p1[0]

    return f"y = {M:.2f}x + {C:.2f}"

# Titik A dan B
A = point(-3, 2)
B = point(-2, 5)

# Menentukan persamaan garis yang melalui titik A dan B
equation = line_equation_of(A, B)

# Menampilkan hasil
print("Persamaan garis yang melalui titik A dan B:")
print(equation)
