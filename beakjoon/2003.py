# 수들의 합 2
import sys
input = sys.stdin.readline
cnt = 0
n, m = map(int, input().split())
li = list(map(int, input().split()))

prefixSum = [0]*(n+1)
l, r = 0, 1
for i in range(n):
    prefixSum[i+1] = prefixSum[i]+li[i]
while l <= r and r <= n:
    v = prefixSum[r]-prefixSum[l]
    if v == m:
        cnt += 1
        r += 1
    elif v < m:
        r += 1

    else:
        l += 1
print(cnt)
