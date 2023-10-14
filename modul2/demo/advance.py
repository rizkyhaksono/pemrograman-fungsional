__author__ = "rizkyhaksono"
__copyright__ = "Copyright 2023, Malang"

import random


def create_board(width):
    # Buat papan permainan dengan lebar sesuai input
    board = [[' ' for _ in range(width)] for _ in range(width)]
    return board


def generate_random_position(width):
    # Generate posisi acak (baris, kolom) dalam rentang 0 hingga width-1
    row = random.randint(0, width - 1)
    col = random.randint(0, width - 1)
    return row, col


def place_piece(board, position, symbol):
    # Letakkan simbol pada posisi tertentu di papan permainan
    row, col = position
    board[row][col] = symbol


def print_board(board):
    # Cetak papan permainan
    for row in board:
        print(' '.join(row))
    print()


def is_valid_move(move, board, position):
    # Cek apakah langkah yang diminta valid
    row, col = position
    if move == 'UP':
        return row > 0 and board[row - 1][col] != '#'
    elif move == 'DOWN':
        return row < len(board) - 1 and board[row + 1][col] != '#'
    elif move == 'LEFT':
        return col > 0 and board[row][col - 1] != '#'
    elif move == 'RIGHT':
        return col < len(board[0]) - 1 and board[row][col + 1] != '#'
    else:
        return False


def move_piece(board, position, move):
    # Pindahkan bidak sesuai dengan langkah yang diminta
    row, col = position
    if move == 'UP':
        board[row][col], board[row - 1][col] = board[row - 1][col], board[row][col]
    elif move == 'DOWN':
        board[row][col], board[row + 1][col] = board[row + 1][col], board[row][col]
    elif move == 'LEFT':
        board[row][col], board[row][col -
                                    1] = board[row][col - 1], board[row][col]
    elif move == 'RIGHT':
        board[row][col], board[row][col +
                                    1] = board[row][col + 1], board[row][col]


def main():
    try:
        width = int(input("Masukkan lebar papan permainan: "))
        if width < 2:
            raise ValueError(
                "Lebar papan permainan harus lebih besar dari atau sama dengan 2.")
    except ValueError as e:
        print(f"Error: {e}")
        return

    board = create_board(width)
    goals = []
    while len(goals) < 3:
        goal_position = generate_random_position(width)
        if goal_position not in goals:
            goals.append(goal_position)

    piece_position = generate_random_position(width)

    for goal in goals:
        place_piece(board, goal, 'O')

    place_piece(board, piece_position, 'A')

    print("Selamat datang di permainan!")
    print("Tujuan Anda adalah mencapai posisi tujuan (O).")
    print_board(board)

    while piece_position not in goals:
        move = input("Masukkan langkah (UP/DOWN/LEFT/RIGHT): ").upper()
        if is_valid_move(move, board, piece_position):
            move_piece(board, piece_position, move)
            print_board(board)
        else:
            print("Langkah tidak valid. Coba lagi.")

    print("Selamat! Anda telah mencapai posisi tujuan (O). Permainan selesai.")


if __name__ == "__main__":
    main()
