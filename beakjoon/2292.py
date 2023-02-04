# 벌집
import sys
input = sys.stdin.readline

room = int(input())

cnt = 1
tmp = 1

while tmp < room:
    tmp += 6*cnt
    cnt += 1

print(cnt)
