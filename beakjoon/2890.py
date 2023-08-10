# 카약
import sys
input = sys.stdin.readline

line, length = map(int, input().split())
maps = []
for l in range(line):
    maps.append(input().strip())
rank = [0 for _ in range(line)]
tmp = 1

for i in range(length-1, 1, -1):
    check = False
    for l in range(line):
        if maps[l][i].isdecimal() and not rank[int(maps[l][i])]:
            check = True
            rank[int(maps[l][i])] = tmp
    if check:
        tmp += 1

for i in range(1, len(rank)):
    if rank[i] != 0:
        print(rank[i])
