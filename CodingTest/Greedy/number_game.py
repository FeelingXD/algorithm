# 숫자 카드 게임
import sys
row, col = map(int, sys.stdin.readline().split())

answer = 0
for i in range(row):
    data = list(map(int, sys.stdin.readline().split()))
    answer = max(answer, min(data))

print(answer)
