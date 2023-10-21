__author__ = "rizkyhaksono"
__copyright__ = "Copyright 2023, Malang"

import random

repeatAll = "y"

# Fungsi untuk membuat board matrix
create_board = lambda width: [["-" for _ in range(width)] for _ in range(width)]

# Fungsi untuk menampilkan board
def display_board(board):
    for row in board:
        print(" ".join(row))

# Fungsi untuk mengacak posisi awal bidak dan tujuan (goals)
def generate_positions(width):
    positions = []
    for _ in range(3):
        x = random.randint(0, width - 1)
        y = random.randint(0, width - 1)
        positions.append((x, y))
    return positions

# Fungsi untuk memeriksa apakah permainan selesai
is_game_over = lambda board, current_pos, goal_pos: (current_pos == goal_pos)

while repeatAll == "y" or repeatAll == "":
    num_attempts = 0
    while num_attempts < 3:
        # Inisialisasi board dengan lebar sesuai input user
        width = int(input("Masukkan lebar board: "))    
        board = create_board(width)

        # Membuat posisi awal bidak dan tujuan secara acak
        try:
            positions = generate_positions(width)
            start_pos, goal_pos = positions[0], positions[1]
            board[start_pos[0]][start_pos[1]] = "A"
            board[goal_pos[0]][goal_pos[1]] = "O"
        except IndexError:
            print("Kesalahan dalam menghasilkan posisi awal dan tujuan.")
        
        if (board[start_pos[0]][start_pos[1]] == board[goal_pos[0]][goal_pos[1]]):
            print("Index A dan 0 Sama")
            print("Generating Ulang ....")
            board[start_pos[0]][start_pos[1]] = "-"
            board[goal_pos[0]][goal_pos[1]] = "-"
            try:
                positions = generate_positions(width)
                start_pos, goal_pos = positions[0], positions[1]
                board[start_pos[0]][start_pos[1]] = "A"
                board[goal_pos[0]][goal_pos[1]] = "O"
            except IndexError:
                print("Kesalahan dalam menghasilkan posisi awal dan tujuan.")
            continue

        display_board(board)

        repeat = input("New Position (Y/N)?").lower()

        ulang = 0

        while repeat == "y":
            board[start_pos[0]][start_pos[1]] = "-"
            board[goal_pos[0]][goal_pos[1]] = "-"
            try:
                positions = generate_positions(width)
                start_pos, goal_pos = positions[0], positions[1]
                board[start_pos[0]][start_pos[1]] = "A"
                board[goal_pos[0]][goal_pos[1]] = "O"
            except IndexError:
                print("Kesalahan dalam menghasilkan posisi awal dan tujuan.")

            if (board[start_pos[0]][start_pos[1]] == board[goal_pos[0]][goal_pos[1]]):
                print("Index A dan 0 Sama")
                print("Generating Ulang ....")
            else:
                display_board(board)
                repeat = input("New Position (Y/N)? ").lower()

                ulang += 1
                if ulang >= 2:
                    print("Maximal 3 dalam mengubah posisi!")
                    repeat = "n"
                    break

        current_pos = start_pos

        move = input("Masukkan perintah (wasd untuk atas/kiri/bawah/kanan, q untuk keluar): ").lower()

        inputList = [char for char in move]
        for list in inputList:
            if list == "q":
                print("Permainan dihentikan.")
                break
            elif list in ["w", "a", "s", "d"]:
                x, y = current_pos
                if list == "w":
                    x -= 1
                elif list == "a":
                    y -= 1
                elif list == "s":
                    x += 1
                elif list == "d":
                    y += 1

                if 0 <= x < width and 0 <= y < width:
                    board[current_pos[0]][current_pos[1]] = "-"
                    current_pos = (x, y)
                    board[current_pos[0]][current_pos[1]] = "A"
                
                else:
                    print("Langkah tidak valid. Coba lagi.")

            else:
                print("Perintah tidak valid. Coba lagi.")

        if is_game_over(board, current_pos, goal_pos):
            display_board(board)
            print("Anda menang! Selamat!")
            break
        else:
            display_board(board)
            print("You Lose!!")
            False
        num_attempts += 1

    repeatAll = input("Apakah Anda ingin mengulang? (y/n): ").lower()
