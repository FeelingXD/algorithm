import heapq

n, k = map(int, input().split())
li = list(map(int, input().split()))
heapq.heapify(li)

for _ in range(k-1):
    heapq.heappop(li)
print(heapq.heappop(li))
