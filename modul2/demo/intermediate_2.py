__author__ = "rizkyhaksono"
__copyright__ = "Copyright 2023, Malang"

import random

def create_board(width):
    # List comprehension
    return [['_'] * width for _ in range(width)]
    

def generate_random_position(width):
    # Generate posisi acak (baris, kolom) dalam rentang 0 hingga width-1
    return (random.randint(0, width - 1), random.randint(0, width - 1))

def place_piece(board, position, symbol):
    # Buat salinan baru dari papan permainan dan letakkan simbol pada posisi tertentu
    new_board = [row[:] for row in board]
    row, col = position
    new_board[row][col] = symbol
    return new_board

def print_board(board):
    # Cetak papan permainan
    for row in board:
        print(' '.join(row))
    print()

def is_valid_move(move, board, position):
    # Cek apakah langkah yang diminta valid
    row, col = position
    if move == 'W':
        return row > 0 and board[row - 1][col] != '#'
    elif move == 'S':
        return row < len(board) - 1 and board[row + 1][col] != '#'
    elif move == 'A':
        return col > 0 and board[row][col - 1] != '#'
    elif move == 'D':
        return col < len(board[0]) - 1 and board[row][col + 1] != '#'
    else:
        return False

def move_piece(board, position, move):
    # Pindahkan bidak sesuai dengan langkah yang diminta
    new_board = place_piece(board, position, ' ')
    row, col = position
    if move == 'W':
        return place_piece(new_board, (row - 1, col), 'A')
    elif move == 'S':
        return place_piece(new_board, (row + 1, col), 'A')
    elif move == 'A':
        return place_piece(new_board, (row, col - 1), 'A')
    elif move == 'D':
        return place_piece(new_board, (row, col + 1), 'A')

def find_piece(board, symbol):
    # Mencari posisi bidak (symbol) pada papan permainan
    for row_idx, row in enumerate(board):
        for col_idx, cell in enumerate(row):
            if cell == symbol:
                return (row_idx, col_idx)
    return None

def edit_piece(board, position, symbol):
    # Mengganti simbol pada posisi tertentu pada papan permainan
    return place_piece(board, position, symbol)

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
    goals = [generate_random_position(width) for _ in range(1)]
    piece_position = generate_random_position(width)

    for goal in goals:
        board = edit_piece(board, goal, 'O')

    board = place_piece(board, piece_position, 'A')

    print("Selamat datang di permainan!")
    print("Tujuan Anda adalah mencapai posisi tujuan (O).")
    print_board(board)

    x = input("New position (Y/N)? ").lower()
    ulang = 0

    while True:
      if x == 'y':
        print("New board generated")

        board = create_board(width)
        goals = [generate_random_position(width) for _ in range(1)]
        piece_position = generate_random_position(width)

        for goal in goals:
            board = edit_piece(board, goal, 'O')

        board = place_piece(board, piece_position, 'A')
        print_board(board)

      elif x == 'n':
        while piece_position not in goals:
          moves = input("Masukkan rangkaian langkah (misal: WASD): ").upper()
          valid = True
          for move in moves:
            if is_valid_move(move, board, piece_position):
              board = move_piece(board, piece_position, move)
              piece_position = find_piece(board, 'A')
            else:
              valid = False
              break

            print_board(board)

            if valid:
                piece_position = find_piece(board, 'A')
            else:
                print("You lose")
                ask = input("Wanna try again?[y/n] ")
                if ask == 'y':
                  main()
                elif ask == 'n':
                  print("Permainan telah dihentikan.")
                  exit()

        print("Selamat! Anda telah mencapai posisi tujuan (O). Permainan selesai.")
      
      if ulang <= 3:
          ulang += 1

      while piece_position not in goals:
          moves = input("Masukkan rangkaian langkah (misal: WASD): ").upper()
          valid = True
          for move in moves:
            if is_valid_move(move, board, piece_position):
              board = move_piece(board, piece_position, move)
              piece_position = find_piece(board, 'A')
            else:
              valid = False
              break

            print_board(board)

            if valid:
                piece_position = find_piece(board, 'A')
            else:
                print("You lose")
                ask = input("Wanna try again?[y/n] ")
                if ask == 'y':
                  main()
                elif ask == 'n':
                  print("Permainan telah dihentikan.")
                  exit()

      print("Selamat! Anda telah mencapai posisi tujuan (O). Permainan selesai.")
    

    # while piece_position not in goals:
    #     moves = input("Masukkan rangkaian langkah (misal: WASD): ").upper()
    #     valid = True
    #     for move in moves:
    #         if is_valid_move(move, board, piece_position):
    #             board = move_piece(board, piece_position, move)
    #             piece_position = find_piece(board, 'A')
    #         else:
    #             valid = False
    #             break

    #     print_board(board)

    #     if valid:
    #         piece_position = find_piece(board, 'A')
    #     else:
    #         print("You lose")
    #         ask = input("Wanna try again?[y/n] ")
    #         if ask == 'y':
    #           main()
    #         elif ask == 'n':
    #           print("Permainan telah dihentikan.")
    #           exit()

    # print("Selamat! Anda telah mencapai posisi tujuan (O). Permainan selesai.")

if __name__ == "__main__":
    main()
