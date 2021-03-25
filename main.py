from enum import Enum
import os

players = ['X', 'O']
unavailable_fields = [1, 2, 3, 4, 5, 6, 7, 8, 9]
row_names = {
    'A': 0,
    'B': 1,
    'C': 2
}
game_field = []
ROWS = COLS = 3
for i in range(ROWS*COLS):
    one_field = [['#', '#', '#'],
                 ['#', '#', '#'],
                 ['#', '#', '#']]
    game_field.append(one_field)

def render_field():
    first_f = 0
    last_f = 3
    field_count = 0
    field_markup = 'ABC'
    print('--1----2----3-------1----2--- 3-------1----2----3----')
    for i in range(0, 3):
        for field in game_field[first_f:last_f]:
            if field[0]:
                print(f'{field[0]} |', end=' ')
        print(field_markup[field_count], end=' ')
        print('\n')
        field_count += 1

        for field in game_field[first_f:last_f]:
            if field[1]:
                print(f'{field[1]} |', end=' ')
        print(field_markup[field_count], end=' ')
        print('\n')
        field_count += 1

        for field in game_field[first_f:last_f]:
            if field[2]:
                print(f'{field[2]} |', end=' ')
        print(field_markup[field_count], end=' ')
        field_count -= 2

        first_f += 3
        last_f += 3
        print('\n--------------------------------------------------------')

def field_winner(player):
    count = 0
    check_x = []
    for field in game_field:
        row = []
        for i in range(3):
            row.append(field[i])
            for y in row:
                check_x.append(y)

        for i in row:
            if len(set(i)) == 1:
                unavailable_fields.append(count)

        collumns = list(zip(*row))
        for i in collumns:
            if len(set(i)) == 1:
                unavailable_fields.append(count)

        if list(set(check_x[::4])) == 1:
            unavailable_fields.append(count)

        if list(set(check_x[-3::-2])[:-1]) == 1:
            unavailable_fields.append(count)

        count += 1

def game_winner()
    pass

def choose_your_field():
    render_field()
    current_field = int(input())
    current_field -= 1
    return current_field

def your_turn():
    current_field = choose_your_field()
    game_ON = True
    os.system('clear')
    while game_ON:
        for player in players:
            render_field()
            turn = input()
            row_name, column = turn
            row_index = row_names[row_name]
            column_index = int(column) - 1
            if current_field in unavailable_fields:
                print('Please choose another field!')
                choose_another_field = True
                while choose_another_field:
                    current_field = choose_your_field()
                    if current_field not in unavailable_fields:
                        choose_another_field = False
            else:
                game_field[current_field][row_index][column_index] = player

                if (row_name == 'A'):
                    current_field = column_index
                if (row_name == 'B'):
                    current_field = column_index + 3
                if (row_name == 'C'):
                    current_field = column_index + 6

            field_winner(player)
            os.system('clear')
your_turn()
