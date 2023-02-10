# 구간 합 구하기4
import sys
input = sys.stdin.readline

nums, cases = map(int, input().split())
li = list(map(int, input().split()))
tot = 0
prefix = [0]
for i in li:
    prefix.append(tot+i)
    tot += i

for _ in range(cases):
    st, end = map(int, input().split())
    print(prefix[end]-prefix[st-1])
