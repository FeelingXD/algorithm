# 게임개발
import sys

n, m = map(int, sys.stdin.readline().split())
d = [[0]*m for _ in range(n)]

x, y, dir = map(int, sys.stdin.readline().split())
d[x][y] = 1  # 현재 좌표 방문 과 동시에 1로변경
cur_area = [x, y]
# 맵정보
array = []
for i in range(n):
    array.append(list(map(int, sys.stdin.readline().split())))

moves = {'0': [-1, 0], '2': [1, 0], '1': [0, 1], '3': [0, -1]}

count = 1
turn_time = 0


def turn_left():
    global dir
    dir -= 1
    if dir == -1:
        dir = 3


while True:
    turn_left()
    nd = [sum(ele) for ele in zip(cur_area, moves[str(dir)])]
    if d[nd[0]][nd[1]] == 0 and array[nd[0]][nd[1]] == 0:
        d[nd[0]][nd[1]] = 1
        cur_area = [nd[0], nd[1]]
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nd = [ele[0]-ele[1] for ele in zip(cur_area, moves[str(dir)])]
        if array[nd[0]][nd[1]] == 0:
            cur_area = [nd[0], nd[1]]
        else:
            break
        turn_time = 0
print(count)
