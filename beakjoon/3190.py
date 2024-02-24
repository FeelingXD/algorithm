# 뱀
import sys
from collections import deque, defaultdict

input = sys.stdin.readline
APPLE = 1
PATH = 0
R = "D"
L = "L"
moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우측부터시작


def check_oob(y, x):  # 보드를 탈출 하는지 검사
    global board
    return 0 <= y < len(board) and 0 <= x < len(board[0])


def snake_game():
    global board, orders
    snake = deque([(0, 0)])
    game_time = 0
    current_d = 0
    cy, cx = 0, 0
    while True:
        if orders[game_time]:
            if orders[game_time] == 1:  # 오른쪽 회전명령
                current_d = (current_d + 1) % 4  # moves를 초과할 수 없음
            else:  # 좌회전의 경우
                current_d = (current_d - 1) % 4
        dy, dx = moves[current_d]
        ny, nx = cy + dy, cx + dx

        if (
            not check_oob(ny, nx) or (ny, nx) in snake
        ):  # 보드 탈출하거나 몸에 부딪힌경우 종료
            break

        if board[ny][nx] != APPLE and snake:
            snake.popleft()
        board[ny][nx] = PATH
        cy, cx = ny, nx
        snake.append((ny, nx))

        game_time += 1

    print(game_time + 1)


def get_board(rows):
    return [[0] * rows for _ in range(rows)]


def solution():
    global board, orders
    n = int(input())  # 맵 크기
    board = get_board(n)
    orders = defaultdict(int)
    for _ in range(apple_len := int(input())):  # 사과 추가
        y, x = map(int, input().split())
        board[y - 1][x - 1] = APPLE
    for _ in range(L := int(input())):  # 명령 추가
        t, order = input().split()
        orders[int(t)] = 1 if order == R else -1
        pass
    snake_game()
    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
