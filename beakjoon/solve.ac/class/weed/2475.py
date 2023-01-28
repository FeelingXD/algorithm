# 검증수
import sys
input = sys.stdin.readline
result = 0
for i in list(map(int, input().split())):
    result += pow(i, 2)
print(result % 10)
