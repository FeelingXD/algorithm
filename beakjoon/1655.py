# 가운데를 말해요
import sys
import heapq
input = sys.stdin.readline
if __name__ == "__main__":
    pass
    right_h = []
    left_h = []
    for _ in range(n := int(input())):
        v = int(input())
        if len(left_h) == len(right_h):
            heapq.heappush(left_h, -v)
        else:
            heapq.heappush(right_h, v)

        if right_h and -left_h[0] > right_h[0]:

            lv = -heapq.heappop(left_h)
            rv = heapq.heappop(right_h)

            heapq.heappush(left_h, -rv)
            heapq.heappush(right_h, lv)
        print(-left_h[0])
