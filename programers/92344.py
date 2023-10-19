# 파괴되지 않은 건물
ATTACK = 1
HEAL = 2


def solution(board, skill):
    answer = 0
    acc_sum = [[0]*(len(board[0])+1) for _ in range(len(board)+1)]
    maps = board
    for cmd in skill:
        c_cmd, y1, x1, y2, x2, degree = cmd
        degree = -degree if c_cmd == ATTACK else degree
        acc_sum[y1][x1] += degree
        acc_sum[y1][x2+1] -= degree
        acc_sum[y2+1][x1] -= degree
        acc_sum[y2+1][x2+1] += degree

    for y in range(len(acc_sum)-1):
        for x in range(len(acc_sum[0])-1):
            acc_sum[y][x+1] += acc_sum[y][x]

    for x in range(len(acc_sum[0])-1):
        for y in range(len(acc_sum)-1):
            acc_sum[y+1][x] += acc_sum[y][x]

    for y in range(len(maps)):
        for x in range(len(maps[0])):
            board[y][x] += acc_sum[y][x]
            if board[y][x] > 0:
                answer += 1

    return answer
