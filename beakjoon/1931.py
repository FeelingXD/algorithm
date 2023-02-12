# 회의실 배정하기
from collections import deque
import sys
input = sys.stdin.readline
q = deque()
case = int(input())
timeTable = []
for i in range(case):
    timeTable.append(tuple(map(int, input().split())))
timeTable.sort(key=lambda x: (x[1], x[0]))


for i in timeTable:
    if not q:
        q.append(i)
    else:
        v = q[-1]
        if i[0] >= v[1]:
            q.append(i)
        continue
print(len(q))
