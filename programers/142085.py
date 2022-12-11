# 디펜스게임

import heapq


def solution(n: int, k: int, enemy: list) -> int:
    heap = []
    sum = 0
    for i in range(len(enemy)):
        heapq.heappush(heap, enemy[i])
        if (len(heap) > k):
            sum += heapq.heappop(heap)
        if (sum > n):
            return i
    return len(enemy)


def solution(n, k, enemy):
    minHeap = enemy[:k]  # [2, 4, 4]
    heapq.heapify(minHeap)
    for i in range(k, len(enemy)):
        heapq.heappush(minHeap, enemy[i])  # push 5, [2, 4, 4, 5]
        n -= heapq.heappop(minHeap)  # pop 2, n = 5
        if n < 0:
            return i
    return len(enemy)
