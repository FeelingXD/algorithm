# 부분수열의 합
import sys
from itertools import combinations
input = sys.stdin.readline
cnt = 0
n, target = map(int, input().split())
numbers = list(map(int, input().split()))
for _ in range(1, len(numbers)+1):
    for i in combinations(numbers, _):
        if sum(i) == target:
            cnt += 1
print(cnt)
