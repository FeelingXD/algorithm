# 주사위 게임
import sys
input = sys.stdin.readline

c, s = 100, 100

for _ in range(int(input())):
    a, b = map(int, input().split())
    if a != b:
        if a > b:
            s -= a
        else:
            c -= b
print(c)
print(s)
