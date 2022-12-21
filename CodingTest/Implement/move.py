# 상하좌우
import sys

x, y = 1, 1
n = int(sys.stdin.readline())
move_queue = list(map(str, sys.stdin.readline().split()))
move_types = {'L': [0, -1], 'R': [0, 1], 'U': [-1, 0], 'D': [1, 0]}
answer = [x, y]
for move in move_queue:

    if (0 not in [sum(n) for n in zip(answer, move_types[move])]) and (n not in [sum(n) for n in zip(answer, move_types[move])]):
        answer = [sum(n) for n in zip(answer, move_types[move])]

print(answer)
