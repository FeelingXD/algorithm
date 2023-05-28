# 빈도정렬
import sys
from collections import Counter
input = sys.stdin.readline

n, k = map(int, input().split())
li = list(map(int, input().split()))
c = Counter(li)
ans = []
for v, r in c.most_common():
    ans += [v]*r
print(*ans)
