# 두용액 메모리초과
# import sys
# from itertools import combinations
# input = sys.stdin.readline

# cases = int(input())
# liquids = list(map(int, input().split()))

# tmp = [[sum(i), i] for i in list(combinations(liquids, 2))]
# tmp.sort(key=lambda x: abs(x[0]))
# print(' '.join(map(str, tmp[0][1])))

# 두 용액
import sys
from itertools import combinations
input = sys.stdin.readline

cases = int(input())
liquids = list(map(int, input().split()))
liquids.sort()

start = 0
end = len(liquids)-1
cur = float("inf")
answer = []
while (start < end):
    total = liquids[start]+liquids[end]

    if total == 0:
        answer = [liquids[start], liquids[end]]
        break

    if abs(cur) > abs(total):
        cur = abs(total)
        answer = [liquids[start], liquids[end]]

    if total < 0:
        start += 1
    else:
        end -= 1
print(answer[0], answer[1])
