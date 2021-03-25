import os

class Hasher:
    def __init__(self, row):
        self.row = row

    def __hash__(self):
        return hash(''.join(self.row))

    def __eq__(self, other):
        return hash(self) == hash(other)

class Board:
    def __init__(self):
        self.field = []
        self.ROWS = self.COLS = 3

    def create_game_field(self):
        for i in range(self.ROWS * self.COLS):
            one_field = [['#', '#', '#'],
                         ['#', '#', '#'],
                         ['#', '#', '#']]
            self.field.append(one_field)
        return self.field

class Render:
    def __init__(self):
        self.first_f = 0
        self.last_f = 3
        self.field_count = 0
        self.field_markup = 'ABC'
        # self.board = Board().create_game_field()

    def render_board(self, board):
        print('--1----2----3-------1----2--- 3-------1----2----3----')
        for i in range(0, 3):
            for field in board[self.first_f:self.last_f]:
                if field[0]:
                    print(f'{field[0]} |', end=' ')
            print(self.field_markup[self.field_count], end=' ')
            print('\n')
            self.field_count += 1

            for field in board[self.first_f:self.last_f]:
                if field[1]:
                    print(f'{field[1]} |', end=' ')
            print(self.field_markup[self.field_count], end=' ')
            print('\n')
            self.field_count += 1

            for field in board[self.first_f:self.last_f]:
                if field[2]:
                    print(f'{field[2]} |', end=' ')
            print(self.field_markup[self.field_count], end=' ')
            self.field_count -= 2

            self.first_f += 3
            self.last_f += 3
            print('\n--------------------------------------------------------')

class Game:
    def __init__(self):
        self.board = Board().create_game_field()
        self.players = ['X', 'O']
        self.unavailable_fields = []
        self.winned_fields = [['#', '#', '#'],
                              ['#', '#', '#'],
                              ['#', '#', '#']]
        self.row_names = {
            'A': 0,
            'B': 1,
            'C': 2
        }
        self.game_field = Render()

    def game_winner(self, player):
        board = self.board
        game_field = self.game_field.render_board(board)
        unavailable_fields = self.unavailable_fields
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

    def choose_your_field(self):
        print('Choose field!')
        current_field = int(input())
        current_field -= 1
        return current_field

    def play(self):
        players = self.players
        unavailable_fields = self.unavailable_fields
        game_field = self.game_field
        current_field = self.choose_your_field()
        row_names = self.row_names
        game_ON = True
        os.system('clear')
        while game_ON:
            for player in players:
                game_field
                turn = input()
                row_name, column = turn
                row_index = row_names[row_name]
                column_index = int(column) - 1
                if current_field in unavailable_fields:
                    print('Please choose another field!')
                    choose_another_field = True
                    while choose_another_field:
                        current_field = self.choose_your_field()
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

                self.game_winner(player)
                os.system('clear')

if __name__ == '__main__':
    start = Game()
    start.play()
