import time

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
        self.boards = [SingleBoard() for i in list(range(9))]
        self.available_boards = list(range(9))

    def move_on_board(self, *args):
        self.boards[args[0]].make_move(args[1], args[2])

    def choose_board(self):
        print(f'Please choose field where you want to make move. Available fields are {self.available_boards} '
              f'starting from left top and going to right. (e.g field 4 is in the 1 column 2 row.):')
        while True:
            current_field = int(input())
            if current_field not in self.available_boards:
                print('Field is out of range or already won by player, please choose another:')
            else:
                return current_field

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

class Game():
    def __init__(self):
        self.PLAYERS = ['X', 'O']
        self.single_board = SingleBoard()
        self.game_board = MultiBoard()

    def start_game(self):
        print('Hello to ultimate tic tac toe made by Darius D.')
        print('To play please type "start"!')
        start = input()

        while True:
            if start == 'start':
                [(print(f'{time.sleep(1)} Game will starts in {3 - i}')) for i in range(3)]
                break
            else:
                print('Type "start please":/')

    def game_loop(self):
        self.start_game()
        current_board = self.game_board.choose_board()
        while True:
            for player in self.PLAYERS:
                print(self.game_board)
                print(f'Please make your turn player {player}. To make turn please choose number of in field.'
                      f'Numbers left {self.single_board.available_moves}:')

                while True:
                    move = int(input())
                    if move not in self.single_board.available_moves:
                        print(f'Wrong input! Please select from available options {self.single_board.available_moves}')
                    else:
                        break

                self.game_board.move_on_board(current_board, move, player)

                if move not in self.game_board.available_boards:
                    current_board = self.game_board.choose_board()
                else:
                    current_board = move

                self.get_single_board_winner(player)

                if self.get_multi_board_winer():
                    break

        print('''
_____                         ____                 
 / ____|                       / __ \                
| |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ 
| | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|
| |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   
 \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   
        ''')

    def get_single_board_winner(self, player):
        boards = []
        for i in range(len(self.game_board.boards)):
            if i in self.game_board.available_boards:
                boards.append(self.game_board.boards[i])

        for board, i in zip(boards, self.game_board.available_boards):
            checking_board = str(self.game_board.boards[i]).split()
            for j in range(3):
                if len(set(checking_board[j*3:j*3 + 3])) == 1:
                    self.game_board.available_boards[i] = player
                if len(set(checking_board[j::3])) == 1:
                    self.game_board.available_boards[i] = player
            if len(set(checking_board[::4])) == 1:
                self.game_board.available_boards[i] = player
            if len(set(checking_board[-3::-2][:-1])) == 1:
                self.game_board.available_boards[i] = player

    def get_multi_board_winer(self):
        for i in range(3):
            if len(set(self.game_board.available_boards[i*3:i*3+3])) == 1:
                return True
            if len(set(self.game_board.available_boards[i::3])) == 1:
                return True
        if len(set(self.game_board.available_boards[::4])) == 1:
            return True
        if len(set(self.game_board.available_boards[-3::-2][:-1])) == 1:
            return True

if __name__ == '__main__':
    game = Game()
    game.game_loop()
