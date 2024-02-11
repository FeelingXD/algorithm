# 감시 dfs
import sys

input = sys.stdin.readline
type_dic = {1: [0], 2: [0, 2], 3: [0, 1], 4: [0, 1, 3], 5: [0, 1, 2, 3]}
WALL = 6
CHECK = 7
PATH = 0
moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def validate_range(row, col):
    return 0 <= row < N and 0 <= col < M


def draw_board(rows: int) -> list:
    """
    :param rows: rows board의 줄의 갯수
    :return: 작성된 board
    """
    return [list(map(int, input().split())) for _ in range(rows)]


def find_cctv(board: list):
    cctvs = []  # type ,cctv pos
    for y in range(len(board)):
        for x in range(len(board[0])):
            if 1 <= board[y][x] < WALL:
                cctvs.append((board[y][x], y, x))  # type, y, x
    return cctvs


def count_path(board):
    global ans
    ans = min(ans, sum(line.count(PATH) for line in board))
    pass


def dfs(cnt: int, board: list) -> None:
    tmp_board = [[board[y][x] for x in range(M)] for y in range(N)]  # deep_copy board
    if cnt == len(cctvs):
        count_path(tmp_board)
        return
    cctv_type, y, x = cctvs[cnt]

    for d in range(4):  # 방향 회전 검사
        marking_board(cctv_type, d, y, x, tmp_board)
        dfs(cnt + 1, tmp_board)
        tmp_board = [[board[y][x] for x in range(M)] for y in range(N)]

    pass


def marking_board(cctv_type: int, d: int, y: int, x: int, tmp_board: list) -> list:
    """
    remark board
    :param:
    cctv_type: cctv 타입
    d: 방향
    y: y좌표
    x: x좌표
    tmp_board: board
    :return:
    board:list
    """
    for v in type_dic[cctv_type]:
        dy, dx = moves[(d + v) % 4]
        cy, cx = y, x
        while True:
            cy += dy
            cx += dx
            if not validate_range(cy, cx) or tmp_board[cy][cx] == WALL:
                break
            if tmp_board[cy][cx]:
                continue
            else:
                tmp_board[cy][cx] = CHECK
    return tmp_board
    pass


def solution():
    global N, M, cctvs, ans
    N, M = map(int, input().split())  # 세로,가로
    board = draw_board(N)
    cctvs = find_cctv(board)
    ans = 999999999

    dfs(0, board)
    print(ans)
    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
# 1234
