__author__ = "rizkyhaksono & rizkyiqbal & yovi & gerald & kharismo"
__copyright__ = "Copyright 2023, CW Coffee"

data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

def curried_converter(weeks):
    def inner_curried(days):
        def inner_inner_curried(hours):
            def final_curried(minutes):
                return [weeks, days, hours, minutes]
            return final_curried
        return inner_inner_curried
    return inner_curried

int_values = []
for item in data:
    parts = item.split()
    weeks = int(parts[0])
    days = int(parts[2])
    hours = int(parts[4])
    minutes = int(parts[6])

    converted_value = curried_converter(weeks)(days)(hours)(minutes)
    int_values.append(converted_value)

print(int_values)
