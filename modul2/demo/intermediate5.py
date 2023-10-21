__author__ = "rizkyhaksono"
__copyright__ = "Copyright 2023, Malang"

import random

def create_board(width):
    return [["-" for _ in range(width)] for _ in range(width)]

def display_board(board):
    return [print(" ".join(row)) for row in board]

def generate_positions(width):
    while True:
        positions = random.sample(range(width * width), 2)
        start_pos, goal_pos = divmod(positions[0], width), divmod(positions[1], width)
        yield start_pos, goal_pos

def is_game_over(board, current_pos, goal_pos):
    return current_pos == goal_pos

def reset_positions(board, positions_generator):
    print("Index A dan O Sama")
    print("Generating Ulang ....")
    board[start_pos[0]][start_pos[1]] = "-"
    board[goal_pos[0]][goal_pos[1]] = "-"
    start_pos, goal_pos = next(positions_generator)
    return initialize_board(board, start_pos, goal_pos)

def main():
    repeat_all = "y"
    while repeat_all in ("y", ""):
        num_attempts = 0
        positions_generator = generate_positions(3)  # generator init
        while num_attempts < 3:
            try:
                width = int(input("Masukkan lebar board: "))
                board = create_board(width)
                start_pos, goal_pos = next(positions_generator)  # generator position
                board[start_pos[0]][start_pos[1]] = "A"
                board[goal_pos[0]][goal_pos[1]] = "O"
            except ValueError:
                print("Masukkan lebar board yang valid.")
                continue

            if board[start_pos[0]][start_pos[1]] == board[goal_pos[0]][goal_pos[1]]:
                reset_positions(board, positions_generator)

            display_board(board)
            repeat = input("New Position (Y/N)? ").lower()
            ulang = 0

            while repeat == "y":
                board[start_pos[0]][start_pos[1]] = "-"
                board[goal_pos[0]][goal_pos[1]] = "-"
                start_pos, goal_pos = next(positions_generator)  # take new generator position
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
    main()
