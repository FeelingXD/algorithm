# 일곱 난쟁이
from itertools import combinations
import sys
input = sys.stdin.readline
heights = []
for _ in '1'*9:
    heights.append(int(input()))

for i in list(combinations(heights, 7)):
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break
