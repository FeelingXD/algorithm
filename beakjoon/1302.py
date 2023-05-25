# 베스트셀러
import sys
from collections import Counter
input = sys.stdin.readline
li = []
for i in range(int(input())):
    li.append(input().strip())

c = Counter(li)
ans = sorted(c.most_common(), key=lambda x: (-x[1], x[0]))

print(ans[0][0])
