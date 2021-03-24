
players = ['X', 'O']
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
    for field in game_field:
        if field[0][0] == field[1][1] and field[1][1] == field[2][2] and field[0][0] != '#': #check X
            return True
        if field[2][0] == field[1][1] and field[1][1] == field[0][2] and field[1][1] != '#': #check X
            return True

        for i in range(3): #check rows
            if ((field[i][0] == field[i][1]) and (field[i][1] == field[i][2]) and (field[i][0] != '#')):
                return True

            check_col = [[], [], []]
            for row in field: # check columns
                check_col[i].append(str(row[i]))
            if (check_col[i][0] == check_col[i][1]) and (check_col[i][1] == check_col[i][2]) and (check_col[i][0] != '#'):
                return True


def your_turn():
    current_field = 0
    game_ON = True
    while game_ON:
        for player in players:
            if field_winner(player):
                game_ON = False

            render_field()
            turn = input()
            row_name, column = turn
            row_index = row_names[row_name]
            column_index = int(column) - 1
            game_field[current_field][row_index][column_index] = player

            if (row_name == 'A'):
                current_field = column_index
            if (row_name == 'B'):
                current_field = column_index + 3
            if (row_name == 'C'):
                current_field = column_index + 6



your_turn()
