"Here is my version of Connect four.Hope you enjoy it :)"


#We globally define rows and columns for future uses:

row_count = 7
col_count = 6


#With the line below we create our class and declare the board, the turns and the last moves:

class connectfour():
    def __init__(self):
        self.board = [[' ' for _ in range(col_count)] for _ in range(row_count)]
        self.turn = 0
        self.last_move = [-1, -1]


#Board condition method defines how the Board will look like and the field of play:
    def boardcondition(self):
        print("\n")
        for o in range(col_count):
            print(f"  ({o + 1}) ", end="")
        print("\n")

        #Here we specifically define the visuals of the board.
        # Note that there will be a seperator | and we will start numbering from 1 instead of 0:

        for r in range(row_count):
            print('#', end="")
            for c in range(col_count):
                print(f"  {self.board[r][c]}  #", end="")
            print("\n")

# Code below checks whether if the game is happening inside the board; Denotes the rules of the edges:
    def limits(self, r, c):
        return (r >= 0 and r < row_count and c >= 0 and c < col_count)

    #here we denote the turns of the players:
    def indicateturn(self):
        player_symbols = ['X', 'O']
        return player_symbols[self.turn % 2]


    def actualturn(self, column):
        # Code below denotes the search from the bottom up to see what fields are available to play so that the turn between players happens:
        for i in range(row_count - 1, -1, -1):
            if self.board[i][column] == ' ':
                self.board[i][column] = self.indicateturn()
                self.last_move = [i, column]

                self.turn = self.turn + 1
                return True

        return False


#code below gives the condition for a winner.In other terms, if there is 4 lines of the same symbol, it means that the winner is indicated:
    def winnerfinder(self):
        final_row = self.last_move[0]
        final_col = self.last_move[1]
        final_letter = self.board[final_row][final_col]

        #here we determine all possible 8 tracks(including diagonal):
        possible_tracks = [[[-1, 0], 0, True],
                      [[1, 0], 0, True],
                      [[0, -1], 0, True],
                      [[0, 1], 0, True],
                      [[-1, -1], 0, True],
                      [[1, 1], 0, True],
                      [[-1, 1], 0, True],
                      [[1, -1], 0, True]]

        #Here we decide how close we are to the last move:
        for a in range(4):
            for d in possible_tracks:
                r = final_row + (d[0][0] * (a + 1))
                c = final_col + (d[0][1] * (a + 1))

                if d[2] and self.limits(r, c) and self.board[r][c] == final_letter:
                    d[1] = d[1] + 1
                else:
                    # Stop searching in this direction
                    d[2] = False

        #Here the paths for 4 pieces in a row is checked:
        for i in range(0, 7, 2):
            if (possible_tracks[i][1] + possible_tracks[i + 1][1] >= 3):
                self.boardcondition()
                print(f"{final_letter} is the winner.Congratulations!!!")
                return final_letter

                # Below is the condition if there are no winners:
        return False


def startplaying():
    #code above and below is used to define the start of the game:
    game = connectfour()

#the code below gives out the condition to continue the game while the game over condition is not met:
    game_ended = False
    while not game_ended:
        game.boardcondition()

        #We ask the user to do the move but also check whether or not if the move is possible:
        possible_move = False

        #We tell the player to insert valid input.Failure to meet the condition will result in the system telling the player to input the right value:
        while not possible_move:
            user_action = input(f"{game.indicateturn()}, please choose a slot from (1-{row_count}): ")
            try:
                possible_move = game.actualturn(int(user_action) - 1)
            except:
                print(f"You are doing it all wrong player!!! please choose the number from 1 to {col_count}")


        #the code below is used to stop the game one the situation of tie:
        if not any(' ' in x for x in game.board):
            print("It is a draw.Friendship has won!!!")
            return

        # We denote that the game should end once the winner is chosen:
        game_ended = game.winnerfinder()

#Below code activates the game
if __name__ == '__main__':
    startplaying()
