# 회사에 있는 사람
from collections import deque
import sys
input = sys.stdin.readline
q = deque()
case = int(input())
table = {}
for _ in range(case):
    v = list(map(str, input().split()))  # v[0] =name, v[1] =status
    table[v[0]] = v[1]

for i in sorted([k for k, v in table.items() if v == 'enter'], reverse=True):
    print(i)
