# 배열 복원하기
import sys

input = sys.stdin.readline


def create_B(rows: int) -> list:
    return [list(map(int, input().split())) for _ in range(rows)]


def print_board(board: list) -> None:
    for line in board:
        print(*line)


def solution() -> None:
    """
    H × W인 배열 A와 두 정수 X와 Y가 있을 때, 크기가 (H + X) × (W + Y)인 배열 B는
    배열 A와 배열 A를 아래로 X칸, 오른쪽으로 Y칸 이동시킨 배열을 겹쳐 만들 수 있다.
    수가 겹쳐지면 수가 합쳐진다.
    """
    H, W, X, Y = map(int, input().split())
    B = create_B(H + X)
    A = [[0] * W for _ in range(H)]
    # B를 탐색
    for j in range(H):
        for i in range(W):
            A[j][i] = (
                B[j][i] - A[j - X][i - Y] if (j - X >= 0 and i - Y >= 0) else B[j][i]
            )

            pass
    print_board(A)
    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
