import os
import time
ROWS = COLS = 3
field_to_play = []
unavailable_fields = []

PLAYER_X = 'X'
PLAYER_O = 'O'

for i in range(ROWS * COLS):
    one_field = [['1#', '4#', '7#'],
                 ['2#', '5#', '8#'],
                 ['3#', '6#', '9#']]
    field_to_play.append(one_field)

game_winner = ['1#', '4#', '7#', '2#', '5#', '8#', '3#', '6#', '9#']

class SingleBoard:
    def __init__(self):
        self.position = list(range(9)) * 9
        self.available_moves = list(range(9))

    def make_move(self, index, player):
        if index not in self.available_moves:
            print(f"Invalid move: {index}. Available moves: {self.available_moves}")
            return

        self.position[index] = player
        self.available_moves.remove(index)

        print(f"Made move: {index}. Position is: {self.position}")

    def __str__(self):
        output = ""

        for i in range(3):
            row = self.position[i*3: i*3 + 3]
            row_strings = [str(elem) for elem in row]

            output += " ".join(row_strings)
            output += "\n"

        return output

class MultiBoard:
    def __init__(self):
        self.boards = [SingleBoard() for i in range(9)]

    def change(self, *args):
        self.boards[args[0]].make_move(args[1], PLAYER_X)

    def __str__(self):
        output = "".join(str(board) for board in self.boards)
        output_rows = output.split("\n")
        output = ''
        for k in range(3):
            for j in range(3):
                row = output_rows[(k*9)+j:(k*9) + (j+9):3]
                output += " | ".join(row)
                output += "\n"

            if k == 0 or k == 1 and k > 0:
                output += "-" * 21
                output += "\n"

        return output

print('step 1')
board = MultiBoard()
board.change(0, 0)
board.change(1, 1)
board.change(2, 2)
board.change(3, 3)
board.change(4, 4)
board.change(5, 5)
board.change(6, 6)
board.change(7, 7)
board.change(8, 8)
print('step 2')
print(board)
print('step 3')

# class Board:
#     def __init__(self):
#         self.field = []
#         self.first_f = 0
#         self.last_f = 3
#         self.field_count = 0
#         self.field_markup = 'ABC'
#
#     def render_board(self):
#         global field_to_play
#         print('--1----2----3-------1----2--- 3-------1----2----3----')
#         for i in range(0, 3):
#             for field in field_to_play[self.first_f:self.last_f]:
#                 if field[0]:
#                     print(f'{field[0]} |', end=' ')
#             print(self.field_markup[self.field_count], end=' ')
#             print('\n')
#             self.field_count += 1
#
#             for field in field_to_play[self.first_f:self.last_f]:
#                 if field[1]:
#                     print(f'{field[1]} |', end=' ')
#             print(self.field_markup[self.field_count], end=' ')
#             print('\n')
#             self.field_count += 1
#
#             for field in field_to_play[self.first_f:self.last_f]:
#                 if field[2]:
#                     print(f'{field[2]} |', end=' ')
#             print(self.field_markup[self.field_count], end=' ')
#             self.field_count -= 2
#
#             self.first_f += 3
#             self.last_f += 3
#             print('\n--------------------------------------------------------')

class Game:
    def __init__(self):
        self.game_field = MultiBoard()
        self.winned_fields = [['#', '#', '#'],
                              ['#', '#', '#'],
                              ['#', '#', '#']]
        self.row_names = {
            'A': 0,
            'B': 1,
            'C': 2
        }

    def field_winner(self, player):
        global field_to_play
        global game_winner
        global unavailable_fields
        count = 0
        for field in field_to_play:
            check_x = []
            row = []
            for i in range(3):
                row.append(field[i])

            for single_row in row:
                for element in single_row:
                    check_x.append(element)

            for i in row:
                if len(set(i)) == 1:
                    unavailable_fields.append(count)
                    game_winner[count] = str(set(i))

            collumns = list(zip(*row))
            for i in collumns:
                if len(set(i)) == 1:
                    unavailable_fields.append(count)
                    game_winner[count] = str(set(i))

            if list(set(check_x[0::4])) == 1:
                unavailable_fields.append(count)
                game_winner[count] = str(set(i))

            if list(set(check_x[-3::-2][:-1])) == 1:
                unavailable_fields.append(count)
                game_winner[count] = str(set(i))

            count += 1

    def game_over(self):
        global game_winner

        if len(set(game_winner[:3])) == 1:
            return True
        elif len(set(game_winner[3:6])) == 1:
            return True
        elif len(set(game_winner[6:9])) == 1:
            return True
        elif len(set(game_winner[::3])) == 1:
            return True
        elif len(set(game_winner[1::3])) == 1:
            return True
        elif len(set(game_winner[2::3])) == 1:
            return True
        elif len(set(game_winner[::4])) == 1:
            return True
        elif len(set(game_winner[-3::-2][:-1])) == 1:
            return True
        else:
            return False


    def choose_your_field(self):
        game_field = self.game_field()
        game_field.render_board()
        print('Choose field!')
        current_field = int(input())
        current_field -= 1
        return current_field

    def play(self):
        global field_to_play
        global players
        global unavailable_fields
        current_field = self.choose_your_field
        row_names = self.row_names
        game_ON = True
        field_number = int(current_field())
        os.system('clear')
        while game_ON:
            for player in players:
                game_field = self.game_field()
                game_field.render_board()

                good_turn = True
                while good_turn:
                    turn = input()
                    row_name, column = turn
                    row_index = row_names[row_name]
                    column_index = int(column) - 1
                    if (field_to_play[field_number][row_index][column_index] == players[0]) or\
                       (field_to_play[field_number][row_index][column_index] == players[1]):
                        print('Wrong Turn!')
                    else:
                        if field_number in unavailable_fields:
                            print('Please choose another field!')
                            choose_another_field = True
                            while choose_another_field:
                                current_field()
                                field_number = current_field()
                                if field_number not in unavailable_fields:
                                    choose_another_field = False
                        else:
                            field_to_play[field_number][row_index][column_index] = player

                            if (row_name == 'A'):
                                field_number = column_index
                            if (row_name == 'B'):
                                field_number = column_index + 3
                            if (row_name == 'C'):
                                field_number = column_index + 6
                        good_turn = False

                self.field_winner(player)
                if self.game_over():
                    print("GAME OVER!!!")
                    time.sleep(10)
                    game_ON = False
                os.system('clear')

# if __name__ == '__main__':
#     start = Game()
#     start.play()
