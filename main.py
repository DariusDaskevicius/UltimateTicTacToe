
game_ON = True
players = ['X', 'O']
game_field = []
for i in range(0, 9):
    one_field = [['1#', '#', '#'],
                 ['2#', '#', '#'],
                 ['3#', '#', '#']]
    game_field.append(one_field)

print(game_field[0][2][0])

def render_field():
    first_f = 0
    last_f = 3
    field_count = 0
    field_markup = 'ABCDEFGHI'
    print(field_markup[2])
    print('--1-----2----3-------4-----5----6-------7-----8----9----')
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
        field_count += 1

        first_f += 3
        last_f += 3
        print('\n--------------------------------------------------------')

def your_turn():
    while game_ON:
        for player in players:
            render_field()
            turn = input()
            if turn == 'A1':
                game_field[0][0][0] = player
            if turn == 'A2':
                game_field[0][0][1] = player
            if turn == 'A3':
                game_field[0][0][2] = player
            if turn == 'B1':
                game_field[0][1][0] = player
            if turn == 'B2':
                game_field[0][1][1] = player
            if turn == 'B3':
                game_field[0][1][2] = player
            if turn == 'C1':
                game_field[0][2][0] = player
            if turn == 'C2':
                game_field[0][2][1] = player
            if turn == 'C3':
                game_field[0][2][2] = player

your_turn()
