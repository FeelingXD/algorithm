# 랜선자르기
import sys
input = sys.stdin.readline

k, n = map(int, input().split())
li = []
for i in range(k):
    li.append(int(input()))
li.sort()
l = 1
r = li[-1]
ans = 0
while l <= r:
    cnt = 0
    mid = (l+r)//2
    for i in li:
        cnt += i//mid

    if cnt >= n:
        ans = max(ans, mid)
        l = mid+1
    else:
        r = mid-1

print(ans)
