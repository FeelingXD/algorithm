#카드 정렬하기
import sys
import heapq
input =sys.stdin.readline

def solution():
    n=int(input())
    heap=[int(input()) for _ in range(n)]
    heapq.heapify(heap)
    ans=[0]
    while len(heap)>1:
        a,b=heapq.heappop(heap),heapq.heappop(heap)
        ans.append(a+b)
        heapq.heappush(heap,a+b)
    print(sum(ans))
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass