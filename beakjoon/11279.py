# 최대힙
import sys
import heapq
input = sys.stdin.readline

case = int(input())

heap = []

for i in range(case):
    cmd = int(input())
    if cmd == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, [-cmd, cmd])
