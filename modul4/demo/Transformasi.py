import math


def transformasi_decorator(trans_func, rot_func, scale_func):
    def decorator(func):
        print("Function address:", func)

        def wrapper(x, y):
            print("Output x:", x)
            print("Output y:", y)
            trans_result = trans_func(x, y)
            print("Translasi result:", trans_result)
            rot_result = rot_func(*trans_result)
            print("Rotasi result:", rot_result)
            scale_result = scale_func(*rot_result)
            print("Dilatasi result:", scale_result)
            return func(*scale_result)

        return wrapper

    return decorator


def translasi(tx, ty):
    # ditambah
    return lambda x, y: (x + tx, y + ty)


def rotasi(sudut):
    # sin cos
    return lambda x, y: (
        x * math.cos(math.radians(sudut)) - y * math.sin(math.radians(sudut)),
        x * math.sin(math.radians(sudut)) + y * math.cos(math.radians(sudut)),
    )


def dilatasi(sx, sy):
    # dikali
    return lambda x, y: (x * sx, y * sy)


def line_equation(x, y, M):
    print("Nilai x:", x)
    print("Nilai y:", y)
    print("Nilai gradient:", M)
    C = y - M * x
    print("Nilai C:", C)
    return f"y = {M:.2f}x + {C:.2f}"


def get_input():
    return (
        float(input("Masukkan inputan nilai x titik A: ")),
        float(input("Masukkan inputan nilai y titik A: ")),
        float(input("Masukkan inputan gradien awal: ")),
        float(input("Masukkan inputan nilai translasi tx: ")),
        float(input("Masukkan inputan nilai translasi ty: ")),
        float(input("Masukkan inputan nilai sudut rotasi: ")),
        float(input("Masukkan inputan nilai skala pada sumbu x: ")),
        float(input("Masukkan inputan nilai skala pada sumbu y: ")),
    )


def main(user_input, trans, rot, dil, eq):
    (
        x_input,
        y_input,
        gradien_awal,
        tx_input,
        ty_input,
        sudut_rotasi,
        sx_input,
        sy_input,
    ) = user_input()

    @transformasi_decorator(
        trans(tx_input, ty_input), rot(sudut_rotasi), dil(sx_input, sy_input)
    )
    def transformed_line_equation(x, y):
        return eq(x, y, gradien_awal)

    result_equation = transformed_line_equation(x_input, y_input)

    print(
        f"Persamaan garis yang melalui titik ({x_input},{y_input}) dan bergradien {gradien_awal:.2f}:"
    )

    print(line_equation(x_input, y_input, gradien_awal))
    print("Persamaan garis baru setelah transformasi:")
    print(result_equation)


if __name__ == "__main__":
    main(get_input, translasi, rotasi, dilatasi, line_equation)
