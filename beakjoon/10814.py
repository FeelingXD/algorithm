# 나이순 정렬
import sys

input = sys.stdin.readline

case = int(input())
li = []
for _ in range(case):
    li.append(list(map(str, input().split())))
li.sort(key=lambda x: int(x[0]))
for i in li:
    print(' '.join(i))
