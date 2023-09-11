# 카드 놀이

import sys
input = sys.stdin.readline

WIN = 3
LOSE = 0
DRAW = 1
if __name__ == "__main__":
    A, B = 0, 0
    lastWin = "D"
    for A_S, B_S in zip(list(map(int, input().split())), list(map(int, input().split()))):
        if A_S > B_S:
            A += WIN
            lastWin = "A"
        elif B_S > A_S:
            B += WIN
            lastWin = "B"
        else:
            A += DRAW
            B += DRAW
    print(A, B)
    print("A" if A > B else "B" if B > A else lastWin)
