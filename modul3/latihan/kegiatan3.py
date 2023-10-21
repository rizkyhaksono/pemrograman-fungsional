__author__ = "rizkyhaksono"
__copyright__ = "Copyright 2023, Malang"

# random_list = #seperti pada kegiatan 1 modul 1
random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

# Filter untuk memisahkan nilai float, int, dan string
float_data = list(filter(lambda x: isinstance(x, float), random_list))
int_data = list(filter(lambda x: isinstance(x, int), random_list))
string_data = list(filter(lambda x: isinstance(x, str), random_list))

# Menghitung berapa banyak angka dalam kategori "ratusan," "puluhan," dan "satuan" dan menampilkan dalam format yang diinginkan
def count_categories(num_list):
    result = {'ratusan': 0, 'puluhan': 0, 'satuan': 0}
    for num in num_list:
        if num >= 100:
            result['ratusan'] += 1
        elif num >= 10:
            result['puluhan'] += 1
        else:
            result['satuan'] += 1
    return result
def pisahInteger(numm_list):
  result = {}
   
  for int in numm_list:
    # print("lol")
    result = []
    for num in num_list:
        num / 100
    return result
    # print(int) 
    # for num in num_list:
    #     if num >= 100:
    #         result['ratusan'] += 1
    #     elif num >= 10:
    #         result['puluhan'] += 1
    #     else:
    #         result['satuan'] += 1
    # return result

# Output
print("Data Float:", float_data)
pisahInteger(int_data)
# print("Data Int:", pisahInteger(int_data))
print("Data String:", string_data)