# 최소비용 구하기
import sys
import heapq
input = sys.stdin.readline
from math import inf

def draw_graph(n,m):
    graph=[[] for _ in range(n+1)]
    #그래프그리기
    for _ in range(m):
        s,e,w=map(int,input().split())
        graph[s].append((e,w))
    
    return graph

def dijkstra(n,st):
    dis=[inf for _ in range(n+1)]
    dis[st]=0
    
    
    # 디익스트라
    q=[]
    heapq.heappush(q,(0,st))# 현재가중치,start
    while q:
        dist,node=heapq.heappop(q)
        if dis[node]<dist:
            continue
        else:
            for next in graph[node]:
                e,w=next
                cost= dis[node]+w
                if cost<dis[e]:
                    dis[e]=cost
                    heapq.heappush(q,(cost,e))
    return dis
    pass
    
def solution():
    global graph
    N=int(input())# 도시갯수
    M=int(input())# 버스의 갯수
    graph=draw_graph(N,M)
    st,t=map(int,input().split())
    dis=dijkstra(N,st)
    print(dis[t])
    
    
    pass

if __name__ =="__main__":
    solution()
    pass