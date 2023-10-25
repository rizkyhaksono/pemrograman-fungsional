__author__ = "rizkyhaksono & rizkyiqbal & yovi & gerald & kharismo"
__copyright__ = "Copyright 2023, CW Coffee"

data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

# Fungsi curried_converter untuk mengonversi nilai integer
def curried_converter(weeks):
    def inner_curried(days):
        def inner_inner_curried(hours):
            def final_curried(minutes):
                return [weeks, days, hours, minutes]
            return final_curried
        return inner_inner_curried
    return inner_curried

# Fungsi untuk memfilter hanya nilai integer dari daftar
def filter_integer_values(item):
    return list(filter(lambda x: x.isdigit(), item.split()))

int_values = []

for item in data:
    integer_values = list(map(int, filter_integer_values(item)))
    weeks = integer_values[0]
    days = integer_values[1]
    hours = integer_values[2]
    minutes = integer_values[3]

    converted_value = curried_converter(weeks)(days)(hours)(minutes)
    int_values.append(converted_value)

print(int_values)