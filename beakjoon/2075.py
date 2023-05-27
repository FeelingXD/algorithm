# N번째로 큰수
import sys
import heapq
input = sys.stdin.readline
li = []
v = int(input())
for i in range(v):
    for i in list(map(int, input().split())):
        print(li)
        if len(li) < v:
            heapq.heappush(li, (i))
        else:
            if li[0] < i:
                heapq.heappop(li)
                heapq.heappush(li, (i))
print(li[0])
