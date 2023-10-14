__author__ = "rizkyhaksono"
__copyright__ = "Copyright 2023, Malang"

expenses = [
    {'tanggal': '2023-07-25', 'deskripsi': 'Makan Siang', 'jumlah': 50000},
    {'tanggal': '2023-07-25', 'deskripsi': 'Transportasi', 'jumlah': 25000},
    {'tanggal': '2023-07-26', 'deskripsi': 'Belanja', 'jumlah': 100000},
]

# TODO 1 Buatlah Fungsi add_expense untuk menambahkan pengeluaran baru ke dalam expenses. Jangan lupa gunakan pure-function
def add_expense(expenses, date, description, amount):
    new_expenses = expenses.copy()
    new_expense = {'tanggal': date, 'deskripsi': description, 'jumlah': amount}
    new_expenses.append(new_expense)
    return new_expenses

# TODO 2 Buatlah fungsi calculate_total_expenses menggunakan lambda expression untuk menghitung total pengeluaran harian.
calculate_total_expenses = lambda expenses: sum(expense['jumlah'] for expense in expenses)

# TODO 3 Buatlah fungsi get_expenses_by_date menggunakan list comprehension untuk menyaring pengeluaran berdasarkan tanggal tertentu.
def get_expenses_by_date(expenses, date):
    return [expense for expense in expenses if expense['tanggal'] == date]

# TODO 4 Buatlah fungsi generate_expenses_report sebagai generator untuk menghasilkan laporan pengeluaran harian dalam bentuk string.
def generate_expenses_report(expenses):
    for expense in expenses:
        yield f"{expense['tanggal']} - {expense['deskripsi']} - Rp {expense['jumlah']}"

def add_expense_interactively(expenses):
    date = input("Masukkan tanggal pengeluaran (YYYY-MM-DD): ")
    description = input("Masukkan deskripsi pengeluaran: ")
    amount = int(input("Masukkan jumlah pengeluaran: "))
    new_expenses = add_expense(expenses, date, description, amount)
    print("Pengeluaran berhasil ditambahkan.")
    return new_expenses

def view_expenses_by_date(expenses):
    date = input("Masukkan tanggal (YYYY-MM-DD): ")
    expenses_on_date = get_expenses_by_date(expenses, date)
    print(f"\nPengeluaran pada tanggal {date}:")
    for expense in expenses_on_date:
        return (f"{expense['deskripsi']} - Rp {expense['jumlah']}")

def view_expenses_report(expenses):
    print("\nLaporan Pengeluaran Harian:")
    expenses_report = generate_expenses_report(expenses)
    listReport = []
    for entry in expenses_report:
        listReport.append(entry)
    return listReport

def display_menu():
    print("\n===== Aplikasi Pencatat Pengeluaran Harian =====")
    print("1. Tambah Pengeluaran")
    print("2. Total Pengeluaran Harian")
    print("3. Lihat Pengeluaran berdasarkan Tanggal")
    print("4. Lihat Laporan Pengeluaran Harian")
    print("5. Keluar")

# TODO 6 ubah fungsi berikut ke dalam bentuk lambda
get_user_input = lambda command: int(input(command))

def main():
    global expenses
    while True:
        display_menu()
        choice = get_user_input("Pilih menu (1/2/3/4/5): ")
        if choice == 1:
            expenses = add_expense_interactively(expenses)
        elif choice == 2:
            total_expenses = calculate_total_expenses(expenses)
            print(f"\nTotal Pengeluaran Harian: Rp {total_expenses}")
        elif choice == 3:
            view_expenses_by_date(expenses)
        elif choice == 4:
            view_expenses_report(expenses)
        elif choice == 5:
            print("Terima kasih telah menggunakan aplikasi kami.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang benar.")

if __name__ == "__main__":
    main()
