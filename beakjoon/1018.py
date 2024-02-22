import sys

input = sys.stdin.readline
BLACK = "B"
WHITE = "W"


def get_board(rows):
    return [input().strip() for _ in range(rows)]


def solution():
    cases = []
    r, c = map(int, input().split())
    board = get_board(r)
    for i in range(r - 7):  # y
        for j in range(c - 7):  # x
            white_case = 0  # 백으로 시작
            black_case = 0  # 흑으로 시작
            for y in range(i, i + 8):
                for x in range(j, j + 8):
                    if (y + x) % 2:  # 원점이 0 일때
                        if board[y][x] == BLACK:  # 블랙케이스
                            white_case += 1
                        else:
                            black_case += 1
                    else:
                        if board[y][x] == BLACK:
                            black_case += 1
                        else:
                            white_case += 1
                        pass
            cases.append(white_case)
            cases.append(black_case)
    print(min(cases))
    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
