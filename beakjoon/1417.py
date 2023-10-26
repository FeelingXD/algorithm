# 국회의원 선거
import sys
import heapq
input = sys.stdin.readline

if __name__ == "__main__":
    case = int(input())
    dasom = int(input())
    cnt = 0
    heap = []
    for _ in range(case-1):
        heap.append(-int(input()))
    heapq.heapify(heap)
    while heap and dasom <= -1*(v := heapq.heappop(heap)):
        heapq.heappush(heap, v+1)
        dasom += 1
        cnt += 1
    print(cnt)
    pass
