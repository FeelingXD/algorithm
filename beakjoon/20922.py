import sys
from collections import defaultdict
input = sys.stdin.readline

n, k = map(int, input().split())
li = list(map(int, input().split()))

dic = defaultdict(int)

ans = 0
l, r = 0, 0
while True:
    if r == n:
        break
    if dic[li[r]] < k:
        dic[li[r]] += 1
        r += 1
    else:
        dic[li[l]] -= 1
        l += 1
    ans = max(r-l, ans)
print(ans)
