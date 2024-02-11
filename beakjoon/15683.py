# 감시
import sys

input = sys.stdin.readline
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


def marking_board(d: int, y: int, x: int) -> None:
    """
    remark board
    :param:
    d: 방향
    y: y좌표
    x: x좌표
    :return:
    None
    """
    global tmp_board
    d %= 4
    dy, dx = moves[d]
    while True:
        y += dy
        x += dx
        if not validate_range(y, x) or tmp_board[y][x] == WALL:
            break
        if tmp_board[y][x]:
            continue
        else:
            tmp_board[y][x] = CHECK

    pass


def solution():
    global N, M, tmp_board
    N, M = map(int, input().split())  # 세로,가로
    board = draw_board(N)
    cctvs = find_cctv(board)
    ans = 999999999

    for case in range(4 ** len(cctvs)):
        tmp_board = [
            [board[y][x] for x in range(M)] for y in range(N)
        ]  # deep_copy board
        tmp_ans = 0
        # remark detection
        for j in range(len(cctvs)):
            d = case % 4
            case //= 4
            cctv_type, y, x = cctvs[j]
            match (cctv_type):
                case 1:
                    marking_board(d, y, x)
                case 2:
                    marking_board(d, y, x)
                    marking_board(d + 2, y, x)
                case 3:
                    marking_board(d, y, x)
                    marking_board(d + 1, y, x)
                case 4:
                    marking_board(d, y, x)
                    marking_board(d + 1, y, x)
                    marking_board(d + 3, y, x)
                case 5:
                    marking_board(d, y, x)
                    marking_board(d + 1, y, x)
                    marking_board(d + 2, y, x)
                    marking_board(d + 3, y, x)
        # 사각지대 검사
        for line in tmp_board:
            tmp_ans += line.count(PATH)
        ans = min(tmp_ans, ans)
    print(ans)
    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
# 1234
