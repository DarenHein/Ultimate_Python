import curses
import random
import time

# Configuración del juego
HEIGHT = 20
WIDTH = 10
DELAY = 0.1

# Piezas del tetromino
tetrominoes = [
    [
        [1, 1, 1, 1]
    ],
    [
        [1, 1],
        [1, 1]
    ],
    [
        [1, 1, 0],
        [0, 1, 1]
    ],
    [
        [0, 1, 1],
        [1, 1, 0]
    ],
    [
        [1, 0, 0],
        [1, 1, 1]
    ],
    [
        [0, 0, 1],
        [1, 1, 1]
    ],
    [
        [1, 1, 1],
        [0, 0, 1]
    ]
]

def draw_window(stdscr):
    stdscr.clear()
    stdscr.border(0)
    stdscr.refresh()

def draw_tetromino(stdscr, tetromino, y, x):
    for row in range(len(tetromino)):
        for col in range(len(tetromino[row])):
            if tetromino[row][col] == 1:
                stdscr.addch(y + row, x + col, "#")

def check_collision(board, tetromino, y, x):
    for row in range(len(tetromino)):
        for col in range(len(tetromino[row])):
            if (
                tetromino[row][col] == 1 and
                (board[y + row][x + col] == "#" or y + row >= HEIGHT or x + col < 0 or x + col >= WIDTH)
            ):
                return True
    return False

def merge_tetromino(board, tetromino, y, x):
    for row in range(len(tetromino)):
        for col in range(len(tetromino[row])):
            if tetromino[row][col] == 1:
                board[y + row][x + col] = "#"

def check_lines(board):
    lines_cleared = 0
    for row in range(HEIGHT):
        if "#" not in board[row]:
            lines_cleared += 1
            del board[row]
            board.insert(0, [" "] * WIDTH)
    return lines_cleared

def main(stdscr):
    curses.curs_set(0)  # Ocultar el cursor
    stdscr.nodelay(1)  # Configurar getch() para que no bloquee la ejecución

    board = [[" "] * WIDTH for _ in range(HEIGHT)]

    tetromino = random.choice(tetrominoes)
    tetromino_y = 0
    tetromino_x = WIDTH // 2 - len(tetromino[0]) // 2

    score = 0

    while True:
        draw_window(stdscr)

        # Mover el tetromino hacia abajo
        if not check_collision(board, tetromino, tetromino_y + 1, tetromino_x):
            tetromino_y += 1
        else:
            merge_tetromino(board, tetromino, tetromino_y, tetromino_x)
            lines_cleared = check_lines(board)
            score += lines_cleared
            tetromino = random.choice(tetrominoes)
            tetromino_y = 0
            tetromino_x = WIDTH // 2 - len(tetromino[0]) // 2

            if check_collision(board, tetromino, tetromino_y, tetromino_x):
                break

        # Mover el tetromino horizontalmente
        key = stdscr.getch()
        if key == curses.KEY_LEFT and not check_collision(board, tetromino, tetromino_y, tetromino_x - 1):
            tetromino_x -= 1
        elif key == curses.KEY_RIGHT and not check_collision(board, tetromino, tetromino_y, tetromino_x + 1):
            tetromino_x += 1

        # Dibujar el tablero y el tetromino
        for row in range(HEIGHT):
            for col in range(WIDTH):
                stdscr.addch(row + 1, col + 1, board[row][col])
        draw_tetromino(stdscr, tetromino, tetromino_y + 1, tetromino_x + 1)

        stdscr.addstr(0, 2, f"Score: {score}")
        stdscr.refresh()

        time.sleep(DELAY)

    stdscr.addstr(HEIGHT // 2, WIDTH // 2 - 5, "GAME OVER")
    stdscr.refresh()
    stdscr.getch()

curses.wrapper(main)
