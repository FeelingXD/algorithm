# 카드 합체 놀이
import sys
import heapq
input =sys.stdin.readline

def solution():
    n,m=map(int,input().split())
    heap=list(map(int,input().split()))
    heapq.heapify(heap)
    for _ in range(m):
        a=heapq.heappop(heap)
        b=heapq.heappop(heap)
        heapq.heappush(heap,a+b)
        heapq.heappush(heap,a+b)
        
    print(sum(heap))
    
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass