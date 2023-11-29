#회장뽑기
import sys
from collections import deque
input =sys.stdin.readline

max_friendship_range=99999
def draw_graph():
    global n
    global graph
    
    n=int(input())
    graph=[[max_friendship_range]*(n+1) for _ in range(n+1)]
    

    while (c:=tuple(map(int,input().split())))!=(-1,-1):
        s,e=c
        graph[s][e]=1
        graph[e][s]=1

def FW():
    # 자기자신은 거리가없으므로 0으로 초기화
    for i in range(1,n+1):
        graph[i][i]=0
    
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if graph[i][j] in (0,1):
                    continue
                elif graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j]= graph[i][k] + graph[k][j]
    
    
def solution():
    draw_graph()
    FW()
    friendship_range=[]
    for i in range(1,n+1):
        friendship_range.append(max(graph[i][1:]))
    
    min_range=min(friendship_range)
    print(min_range,friendship_range.count(min_range))
    for i,v in enumerate(friendship_range):
        if v==min_range:
            print(i+1,end=" ")

    pass
if __name__=="__main__": # 실행되는 부분
    
    solution()
    pass