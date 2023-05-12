# 꿀아르바이트
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
li = list(map(int, input().split()))

step = m
window = sum(li[:step])
ans = window
for i in range(step, n):
    window += li[i]-li[i-step]
    ans = max(ans, window)
print(ans)
