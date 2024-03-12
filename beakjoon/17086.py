# 아기 상어 2
import sys
from collections import deque

input = sys.stdin.readline
moves = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]

PATH = 0
SHARK = 1


def draw_board(row):
    return [list(map(int, input().split())) for _ in range(row)]


def shark_pos(board):  # 상어의 위치들
    poses = []
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x]:
                poses.append((y, x))
    return poses


def check_oob(ny, nx):
    return 0 <= ny < r and 0 <= nx < c


def bfs(
    safe_score, shark_poses
):  # 각 상어 좌표를 시작으로 각각의 안전거리를 만들어준다.
    """
    @param
    safe_score : 안전거리를 기록할 보드
    shark_poses : 상어 위치를 기록한 좌표들
    """
    for shark in shark_poses:
        q = deque()
        q.append(shark)
        while q:
            cy, cx = q.popleft()
            for dy, dx in moves:
                ny, nx = cy + dy, cx + dx
                if not check_oob(ny, nx):
                    continue
                if board[ny][nx] == PATH:
                    if (
                        not safe_score[ny][nx]
                        or safe_score[cy][cx] + 1 < safe_score[ny][nx]
                    ):
                        safe_score[ny][nx] = safe_score[cy][cx] + 1
                        q.append((ny, nx))
                pass
            pass
    # 안전거리 최대값 계산하기
    ans = 0
    for line in safe_score:
        ans = max(max(line), ans)
    return ans


def board_print(board):
    for line in board:
        print(line)


def solution():
    global r, c, board
    r, c = map(int, input().split())
    board = draw_board(r)
    safe_score = [[0] * len(board[0]) for _ in range(r)]
    shark_poses = shark_pos(board)
    print(bfs(safe_score, shark_poses))
    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
