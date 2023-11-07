#경로 찾기
import sys
from collections import deque
input = sys.stdin.readline

def search_node(n):
    visited = [0]*len(graph)
    q=deque()
    q.append(n)
    
    while q:
        v=q.popleft()
        for n in range(len(graph[v])):
            if graph[v][n]==1:
                if not visited[n]:
                    visited[n]=1
                    q.append(n)
    print(*visited)
     

def solution():
    n=int(input())
    global graph
    graph=[]
    # 그래프 그리기
    for _ in range(n):
        graph.append(list(map(int,input().split())))    
    for i in range(n):
        search_node(i)

if __name__ =="__main__":
    solution()