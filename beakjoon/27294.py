# 	몇개고?
import sys
input = sys.stdin.readline

t, s = map(int, input().split())

if 12 <= t <= 16:
    if s:
        print(280)
    else:
        print(320)
else:
    print(280)
