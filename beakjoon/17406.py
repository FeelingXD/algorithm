# 배열 돌리기 4
import sys

input = sys.stdin.readline


def get_board(rows):
    """
    보드를 만드는 함수
    """
    return [list(map(int, input().split())) for _ in range(rows)]


def rotate_board(board, args):
    """
    보드를 회전하는 함수
    → ↓ ← ↑
    """
    copy_board = [line[:] for line in board]
    r, c, s = args
    for i in range(1, s + 1):
        # 상단 → 이동
        for x in range(c - i, c + i):
            copy_board[r - i][x + 1] = board[r - i][x]
        # 우측 ↓ 이동
        for y in range(r - i, r + i):
            copy_board[y + 1][c + i] = board[y][c + i]
        # 하단 ← 이동
        for x in range(c + i, c - i, -1):
            copy_board[r + i][x - 1] = board[r + i][x]
        # 좌측 ↑ 이동
        for y in range(r + i, r - i, -1):
            copy_board[y - 1][c - i] = board[y][c - i]
        pass
    return copy_board
    pass


def dfs(cnt, board):
    global ans
    if cnt == K:
        ans = min(ans, min(sum(line) for line in board))
    else:
        for i in range(K):
            if not visited[i]:
                visited[i] = True
                dfs(cnt + 1, rotate_board(board, orders[i]))
                visited[i] = False


def solution():
    global orders, visited, K, ans
    N, M, K = map(int, input().split())
    ans = 10e9  # 정답 초기값을 큰값으로 초기화
    board = get_board(N)
    orders = [tuple(map(int, input().split())) for _ in range(K)]
    orders = list(map(lambda x, y, c: (x - 1, y - 1, c), *zip(*orders)))
    visited = [False] * K
    dfs(0, board)
    print(ans)
    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
