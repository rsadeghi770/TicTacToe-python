

def main():
    board = [' '] * 9

    # state
    done = False
    playerX = True

    # loop:
    while not done:
        # draw the board
        print(f"""
 {board[0]} | {board[1]} | {board[2]}
---+---+---
 {board[3]} | {board[4]} | {board[5]}
---+---+---
 {board[6]} | {board[7]} | {board[8]} """)


        """"
        |
        |           o |
        |           o |
        |           o |
        | x         o |
        | x . . . . o |                   |
        +--------------------+
          0 1 2 3 4 5  
        """

        # take an input
        while True:
            index = input()
            try:
                int_index = int(index)
            except:
                continue
            index_good = (0 <= int_index < 9)

            if index_good:
                break


        board[int(index)] = 'x' if playerX else 'o'

        # check win
        win_conditions = [
            (0, 1, 2),
            (3, 4, 5),
            (5, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6)
        ]

        for x, y, z in win_conditions:
            if board[x] == board[y] == board[z] and board[x] != " ":
                done = True

        # switch turn
        playerX = not playerX






#
#
#   x | o | o
#  ---+---+---
#   x | o |
#  ---+---+---
#   o | x |
#
#
#
#
#

if __name__ == '__main__':
    main()