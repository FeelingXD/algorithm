# 보석도둑
import sys
import heapq
input = sys.stdin.readline


if __name__ == "__main__":
    n, k = map(int, input().split())
    jewels = [list(map(int, input().split()))for _ in range(n)]
    bags = [int(input()) for _ in range(k)]
    jewels.sort()
    bags.sort()
    tmp = []
    answer = 0
    for bag in bags:
        while jewels and bag >= jewels[0][0]:  # m,v = 무게 ,가치
            heapq.heappush(tmp, -jewels[0][1])
            heapq.heappop(jewels)
        if tmp:
            answer += heapq.heappop(tmp)
    print(-answer)
    pass
