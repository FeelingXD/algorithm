# 로또
from itertools import combinations
import sys
input = sys.stdin.readline
while True:
    tmp = list(map(int, input().split()))
    if tmp[0] == 0:
        break
    for i in combinations(tmp[1:], 6):
        print(' '.join([str(x) for x in i]))
    print()
