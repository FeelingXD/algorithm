# 이중 우선순위 큐
import heapq
import sys
input = sys.stdin.readline
t = int(input())


for i in range(t):

    k = int(input())
    deleted = [True]*k

    max_heap = []
    min_heap = []
    for i in range(k):

        com, n = input().split()
        n = int(n)
        if com == 'I':
            heapq.heappush(min_heap, (n, i))
            heapq.heappush(max_heap, (-n, i))
            deleted[i] = False
        else:
            if n == 1:  # 최대값을 삭제
                while max_heap and deleted[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    deleted[max_heap[0][1]] = True
                    heapq.heappop(max_heap)
            else:  # -1 일경우
                while min_heap and deleted[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    deleted[min_heap[0][1]] = True
                    heapq.heappop(min_heap)
        while min_heap and deleted[min_heap[0][1]]:
            heapq.heappop(min_heap)
        while max_heap and deleted[max_heap[0][1]]:
            heapq.heappop(max_heap)

    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")
