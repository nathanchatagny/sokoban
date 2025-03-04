COLOR_BOX = "\033[0;33;40m"   # Yellow
COLOR_BOX_ON_GOAL = "\033[1;36;40m"  # Cyan
COLOR_PLAYER = "\033[1;32;40m"  # Green
COLOR_PLAYER_ON_GOAL = "\033[0;31;40m"  # Red
COLOR_WALL = "\033[0;34;40m"  # Bold Blue
COLOR_GOAL = "\033[0;35;40m"  # Magenta
COLOR_FLOOR = "\033[0;30;40m"  # Invisible
COLOR_RESET = "\033[0m"  # Reset to default

SYMBOL_BOX = "$"
SYMBOL_BOX_ON_GOAL = "*"
SYMBOL_PLAYER = "@"
SYMBOL_PLAYER_ON_GOAL = "+"
SYMBOL_GOAL = "."
SYMBOL_WALL = "#"
SYMBOL_FLOOR = "-"

symbolColorMapping = {
    SYMBOL_BOX: COLOR_BOX,
    SYMBOL_BOX_ON_GOAL: COLOR_BOX_ON_GOAL,
    SYMBOL_PLAYER: COLOR_PLAYER,
    SYMBOL_PLAYER_ON_GOAL: COLOR_PLAYER_ON_GOAL,
    SYMBOL_WALL: COLOR_WALL,
    SYMBOL_GOAL: COLOR_GOAL,
    SYMBOL_FLOOR: COLOR_FLOOR,
}

def read_file(xsb_file):
    with open(xsb_file, "r") as f:
        return [list(line.strip()) for line in f]

def print_board_color(board):
    for row in board:
        colored_row = "".join(symbolColorMapping[cell] + cell for cell in row)
        print(colored_row + COLOR_RESET)

def getPlayerPosition(board):
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell in {SYMBOL_PLAYER, SYMBOL_PLAYER_ON_GOAL}:
                return (y, x)
    return None

def isEmpty(board, y, x):
    return board[y][x] in {SYMBOL_FLOOR, SYMBOL_GOAL}

def isBox(board, y, x):
    return board[y][x] in {SYMBOL_BOX, SYMBOL_BOX_ON_GOAL}

def move(board, dy, dx):
    y, x = getPlayerPosition(board)
    ny, nx = y + dy, x + dx  # Nouvelle position du joueur

    # Vérifier si le mouvement est en dehors des limites
    if not (0 <= ny < len(board) and 0 <= nx < len(board[0])):
        return "Can't move outside board"

    if isEmpty(board, ny, nx):  # Si la case est vide, déplacer le joueur
        board[ny][nx] = SYMBOL_PLAYER_ON_GOAL if board[ny][nx] == SYMBOL_GOAL else SYMBOL_PLAYER
        board[y][x] = SYMBOL_GOAL if board[y][x] == SYMBOL_PLAYER_ON_GOAL else SYMBOL_FLOOR

    elif isBox(board, ny, nx):  # Si c'est une boîte, vérifier si on peut la pousser
        nny, nnx = ny + dy, nx + dx  # Nouvelle position de la boîte

        if not (0 <= nny < len(board) and 0 <= nnx < len(board[0])):
            return "Can't push the box outside board"

        if isEmpty(board, nny, nnx):  # Si la case après la boîte est vide
            board[nny][nnx] = SYMBOL_BOX_ON_GOAL if board[nny][nnx] == SYMBOL_GOAL else SYMBOL_BOX
            board[ny][nx] = SYMBOL_PLAYER_ON_GOAL if board[ny][nx] == SYMBOL_BOX_ON_GOAL else SYMBOL_PLAYER
            board[y][x] = SYMBOL_GOAL if board[y][x] == SYMBOL_PLAYER_ON_GOAL else SYMBOL_FLOOR
        else:
            return "A wall or another box is blocking the way"
    else:
        return "Can't move there"

board = read_file("level1.xsb")
print_board_color(board)

move_map = {'w': (-1, 0), 'a': (0, -1), 's': (1, 0), 'd': (0, 1)}

while True:
    player_movement = input("Enter move (w, a, s, d): ").strip().lower()
    if player_movement in move_map:
        invalid = move(board, *move_map[player_movement])
        if not invalid:
            print_board_color(board)
        else:
            print("Invalid move:", invalid)
    else:
        print("Invalid input! Use 'w', 'a', 's', or 'd'.")