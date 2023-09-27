__author__ = "rizkyhaksono"
__copyright__ = "Copyright 2023, Malang"

random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

int_dict = {}
float_tuple = ()
str_list = []

for item in random_list:
    if isinstance(item, int):
        # Pisahkan angka menjadi satuan, puluhan, dan ratusan
        satuan = item % 10
        puluhan = (item // 10) % 10
        ratusan = item // 100
        int_dict[item] = {"ratusan": ratusan,
                          "puluhan": puluhan, "satuan": satuan}
    elif isinstance(item, float):
        # Masukkan float ke dalam tuple

        # memakai koma karena concat hanya bisa di tuple, di float tidak bisa
        float_tuple += (item,)
    elif isinstance(item, str):
        # Masukkan string ke dalam list
        str_list.append(item)

print("Data int dalam bentuk dictionary:", int_dict, end='\n\n')
print("Data float dalam bentuk tuple:", float_tuple, end='\n\n')
print("Data string dalam bentuk list:", str_list, end='')
