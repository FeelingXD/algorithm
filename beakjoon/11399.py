# ATM
import sys
import heapq
input = sys.stdin.readline

n = int(input())
t = 0
ans = 0
li = sorted(list(map(int, input().split())))
for i in li:
    t += i
    ans += t
print(ans)
