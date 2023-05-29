# 과자 나눠주기
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
li = list(map(int, input().split()))
ans = 0
l, r = 1, int(1e9)
while l <= r:
    cnt = 0

    mid = (l+r)//2
    if mid == 0:
        print(0)
        exit()

    for i in li:
        cnt += i//mid
    if cnt >= n:
        ans = max(ans, mid)
        l = mid+1
    else:
        r = mid-1

print(ans)
