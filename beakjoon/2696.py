#중앙값 구하기
import sys
import heapq
input=sys.stdin.readline


def solution():
    li=[]
    n=int(input())
    n=n//10+1 if n%10 else n//10
    for _ in range(n):
        li+=list(map(int,input().split()))    
    
    max_h=[]
    min_h=[]
    answer=[]
    cnt=1
    for v in li:
        if len(max_h)==len(min_h):
            heapq.heappush(max_h,-v)
        else:
            heapq.heappush(min_h,v)
        
        if min_h and max_h and min_h[0]<-max_h[0]:
            max_v =-heapq.heappop(max_h)
            min_v =heapq.heappop(min_h)
            
            heapq.heappush(min_h,max_v)
            heapq.heappush(max_h,-min_v)
        if cnt%2:
            answer.append(-max_h[0])
        cnt+=1
    print(len(answer))
    
    for v in range(0,len(answer),10):
        print(*answer[v:v+10])

if __name__=="__main__":
    for _ in range(n:=int(input())):
        solution()
    pass