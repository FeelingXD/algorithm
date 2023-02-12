# 멀티탭 충분하니 ?
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
plugs = list(map(int, input().split()))
available = 0
for i in plugs:
    if i % 2 == 1:
        available += i//2+1
    else:
        available += i//2
print('YES' if available >= N else 'NO')
