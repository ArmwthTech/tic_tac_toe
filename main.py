import random


def greet():
    # Функция для печати приветствия и
    print("-------------------")
    print("  Приветсвуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")


def print_board(board):
    # Функция для печати текущего состояния игрового поля
    print("  1 2 3")
    for i in range(3):
        print(f"{i + 1} {' '.join(board[i])}")


def check_winner(board):
    # Проверка на победителя по строкам, столбцам и диагоналям
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '-':
            return True
        if board[0][i] == board[1][i] == board[2][i] != '-':
            return True
    if board[0][0] == board[1][1] == board[2][2] != '-':
        return True
    if board[0][2] == board[1][1] == board[2][0] != '-':
        return True
    return False


def is_board_full(board):
    # Проверка, заполнена ли доска
    for row in board:
        if '-' in row:
            return False
    return True


def get_user_move():
    # Получение хода от пользователя
    while True:
        cords = input("Ваш ход:").split()

        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue

        row, col = cords

        if not (row.isdigit()) or not (col.isdigit()):
            print(" Введите числа! ")
            continue

        row, col = int(row), int(col)

        if 0 > row or row > 3 or 0 > col or col > 3:
            print(" Координаты вне диапазона! ")
            continue
        break

    return row-1, col-1


def get_computer_move(board):
    # Получение случайного хода от компьютера
    available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == '-']
    return random.choice(available_moves) if available_moves else (None, None)


def tic_tac_toe():
    # Основная функция для игры в крестики-нолики
    board = [['-' for _ in range(3)] for _ in range(3)]
    count = 0

    while True:
        print_board(board)
        # Выбор режима игры
        while True:
            choice = input("Выберите режим игры (1 - с компьютером, 2 - с другим игроком): ")
            if choice in ('1', '2'):
                break
            else:
                print("Некорректный выбор. Пожалуйста, введите 1 или 2.")

        player_symbols = ['X', 'O']
        current_player = player_symbols[0]

        while True:
            print_board(board)

            if current_player == 'X' or (current_player == 'O' and choice == '2'):
                print(f'Ходит {current_player}')
                row, col = get_user_move()
            else:
                print(f'Ходит {current_player}')
                row, col = get_computer_move(board)

            if row is None or col is None:
                print("Игра завершена.")
                break

            if board[row][col] == '-':
                board[row][col] = current_player
            else:
                print("Эта клетка уже занята. Попробуйте снова.")
                continue

            if check_winner(board):
                print_board(board)
                print(f"Игрок {current_player} победил!")
                break

            if is_board_full(board):
                print_board(board)
                print("Ничья!")
                break

            current_player = player_symbols[1] if current_player == player_symbols[0] else player_symbols[0]



if __name__ == "__main__":
    greet()
    tic_tac_toe()
