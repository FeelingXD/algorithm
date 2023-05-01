# N queen
import sys
input = sys.stdin.readline

answer = 0
n = int(input())
board = [0]*n


def promise(cdx):
    for i in range(cdx):
        if board[cdx] == board[i] or cdx-i == abs(board[cdx]-board[i]):
            return False
    return True


def nqueen(cdx):
    global answer
    if cdx == n:
        print(board)
        answer += 1
        return
    else:
        for i in range(n):
            board[cdx] = i
            if promise(cdx):
                nqueen(cdx+1)


nqueen(0)
print(answer)
