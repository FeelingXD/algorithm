# 절대값 힙
import sys
import heapq
input = sys.stdin.readline
li = []
ans = []
for _ in range(int(input())):
    cmd = int(input())
    if cmd == 0:
        if not len(li):
            print(0)
        else:
            v = heapq.heappop(li)[1]
            print(v)

    else:
        heapq.heappush(li, ([abs(cmd), cmd]))
