# 팩토리얼 0의 개수
import sys
input = sys.stdin.readline
cnt = 0
total = 1


def facto(n):
    global total
    for i in range(1, n+1):
        total *= i
    return total


n = int(input())

for i in str(facto(n))[::-1]:
    if i == '0':
        cnt += 1
    else:
        break
print(cnt)
