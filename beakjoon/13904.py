# 과제
import heapq
import sys
input =sys.stdin.readline

def solution():
    visited=[False]*1001
    heap=[]
    ans=0
    for _ in range(int(input())):
        d,v=map(int,input().split())
        heapq.heappush(heap,(-v,d))
    while heap:
        v,d = heapq.heappop(heap)
        for i in range(d,0,-1):
            if not visited[i]:
                visited[i]=True
                ans+=-v
                break
    print(ans)
    
    
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass