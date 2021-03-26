PLAYER_X = 1
PLAYER_O = -1

class SingleBoard:
    def __init__(self):
        self.position = [0] * 9
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
        self.boards[0].make_move(0, PLAYER_X)
        self.boards[1].make_move(1, PLAYER_X)
        self.boards[2].make_move(2, PLAYER_X)
        self.boards[3].make_move(3, PLAYER_X)
        self.boards[4].make_move(4, PLAYER_X)
        self.boards[5].make_move(5, PLAYER_X)
        self.boards[6].make_move(6, PLAYER_X)
        self.boards[7].make_move(7, PLAYER_X)
        self.boards[8].make_move(8, PLAYER_X)

    def __str__(self):

        # join all boards together one after another
        # Example
        """
        1 0 0 -> Board 1
        0 0 0
        0 0 0
        0 1 0 -> Board 2
        0 0 0
        0 0 0
        0 0 1 -> Board 3
        0 0 0
        0 0 0
        """
        output = "".join(str(board) for board in self.boards)

        # Split overall string on every new line
        # Example
        """
        [
            ["1 0 0"] -> Board 1
            ["0 0 0"]
            ["0 0 0"]
            ["0 1 0"] -> Board 2
            ["0 0 0"]
            ["0 0 0"]
            ["0 0 1"] -> Board 3
            ["0 0 0"]
            ["0 0 0"]
        ]
        """
        output_rows = output.split("\n")

        for i in range(9):
            # Take every third board to form the rows of the BIG tic tac toe
            # Example
            """
            [
            ["1 0 0"] --> Board 1
            ["0 0 0"] -Skip
            ["0 0 0"] -Skip
            ["0 1 0"] --> Board 2
            ["0 0 0"] -Skip
            ["0 0 0"] -Skip
            ["0 0 1"] --> Board 3
            ["0 0 0"] -Skip
            ["0 0 0"] -Skip
            ]
            """
            # Make sure to only take 3 of these at a time because 3 small rows form 1 row of the big board
            row = output_rows[i::3][:3]

            # Separate each sub-board with a pipe character
            output += " | ".join(row)  # row = ["1 0 0", "0 1 0", "0 0 1"]
            # Add newline after each row of the BIG board
            output += "\n"

            if i % 2 == 0 and i>0:
                output += "-" * 21
                output += "\n"

        # output = "\n\n".join(str(board) for board in self.boards)

        return output


board = MultiBoard()
print(board)

# board = SingleBoard()
# print("Initial board", board.position, "Available moves", board.available_moves)

# board.make_move(0, PLAYER_X)
# board.make_move(0, PLAYER_O)

# print(board)
