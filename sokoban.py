from colorama import Fore, Style

play_board = open("/Users/nathanchatagny/Desktop/EPFL/Programming and software/Sokoban game/level1.xsb", "r").read().strip().splitlines()


def getPlayerPosition(play_board):
    for row in range(len(play_board)):
        for col in range(len(play_board[row])):
            if play_board[row][col] == "@":
                return (row, col)
    return None

def isEmpty(row, col):
    if play_board[row][col] == "-" or play_board[row][col] == ".":
        return True
    return None

def isBox(row, col):
    if play_board[row][col] == "$" or play_board[row][col] == "*":
        return True
    return None

def printBoard():
    color_map = {
        "#": Fore.LIGHTBLACK_EX,
        "@": Fore.GREEN,
        "+": Fore.GREEN + Style.BRIGHT,
        "$": Fore.YELLOW,
        "*": Fore.MAGENTA,
        ".": Fore.CYAN,
        " ": Fore.WHITE
    }

    for row in play_board:
        colored_row = "".join(color_map.get(char, Fore.WHITE) + char for char in row)
        print(colored_row)
printBoard()

player_position = getPlayerPosition(play_board)
if player_position:
    print(f"Player is at position: {player_position}")
else:
    print("Player not found!")