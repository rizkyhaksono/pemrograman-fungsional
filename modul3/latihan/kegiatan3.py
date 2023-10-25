__author__ = "rizkyhaksono & rizkyiqbal & yovi & gerald & kharismo"
__copyright__ = "Copyright 2023, Malang, Lab A&B"

random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

def separate_int(item):
    if isinstance(item, int):
        satuan = item % 10
        puluhan = (item // 10) % 10
        ratusan = item // 100
        return (item, {"ratusan": ratusan, "puluhan": puluhan, "satuan": satuan})
    else:
        return item

int_list = list(filter(lambda x: isinstance(x, tuple), map(separate_int, random_list)))

float_tuple = tuple(filter(lambda item: isinstance(item, float), random_list))

str_list = list(filter(lambda item: isinstance(item, str), random_list))

print("Data int dalam bentuk list of tuples:", int_list, end='\n\n')
print("Data float dalam bentuk tuple:", float_tuple, end='\n\n')
print("Data string dalam bentuk list:", str_list)
