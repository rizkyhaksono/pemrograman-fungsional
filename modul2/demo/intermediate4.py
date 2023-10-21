__author__ = "rizkyhaksono"
__copyright__ = "Copyright 2023, Malang"

import random

# Fungsi untuk membuat board matrix
# Pure Function, List Comprehension
def create_board(width):
    return [["-" for _ in range(width)] for _ in range(width)]

# Fungsi untuk menampilkan board
def display_board(board):
    for row in board:
        print(" ".join(row))

# Fungsi untuk menghasilkan posisi awal bidak dan tujuan secara acak
# Iterator Generator
def generate_positions(width):
    positions = random.sample(range(width * width), 2)
    start_pos, goal_pos = divmod(positions[0], width), divmod(positions[1], width)
    print(positions, start_pos)
    return start_pos, goal_pos

# Fungsi untuk memeriksa apakah permainan selesai
def is_game_over(board, current_pos, goal_pos):
    return current_pos == goal_pos

def play_game():
    repeat_all = "y"
    while repeat_all in ("y", ""):
        num_attempts = 0
        while num_attempts < 3:
            try:
                width = int(input("Masukkan lebar board: "))
                board = create_board(width)
                start_pos, goal_pos = generate_positions(width)
                board[start_pos[0]][start_pos[1]] = "A"
                board[goal_pos[0]][goal_pos[1]] = "O"
            except ValueError:
                print("Masukkan lebar board yang valid.")
                continue

            if board[start_pos[0]][start_pos[1]] == board[goal_pos[0]][goal_pos[1]]:
                print("Index A dan O Sama")
                print("Generating Ulang ....")
                board[start_pos[0]][start_pos[1]] = "-"
                board[goal_pos[0]][goal_pos[1]] = "-"
                start_pos, goal_pos = generate_positions(width)
                board[start_pos[0]][start_pos[1]] = "A"
                board[goal_pos[0]][goal_pos[1]] = "O"

            display_board(board)
            repeat = input("New Position (Y/N)? ").lower()
            ulang = 0

            while repeat == "y":
                board[start_pos[0]][start_pos[1]] = "-"
                board[goal_pos[0]][goal_pos[1]] = "-"
                start_pos, goal_pos = generate_positions(width)
                board[start_pos[0]][start_pos[1]] = "A"
                board[goal_pos[0]][goal_pos[1]] = "O"

                if board[start_pos[0]][start_pos[1]] == board[goal_pos[0]][goal_pos[1]]:
                    print("Index A dan O Sama")
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

            while True:
                move = input("Masukkan perintah (wasd untuk atas/kiri/bawah/kanan, q untuk keluar): ").lower()
                input_list = [char for char in move]

                for char in input_list:
                    if char == "q":
                        print("Permainan dihentikan.")
                        return

                    if char in ["w", "a", "s", "d"]:
                        x, y = current_pos
                        if char == "w":
                            x -= 1
                        elif char == "a":
                            y -= 1
                        elif char == "s":
                            x += 1
                        elif char == "d":
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
                    return
                else:
                    display_board(board)
                    print("You Lose!!")
                    return
            num_attempts += 1

        repeat_all = input("Apakah Anda ingin mengulang? (y/n): ").lower()

if __name__ == "__main__":
    play_game()
