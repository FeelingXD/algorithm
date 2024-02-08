# 축사 배정
import sys
input =sys.stdin.readline

def dfs(node:int):
    if visited[node]:
        return False
    visited[node]=True    
    for room in cows[node]:
        if rooms[room]==-1 or dfs(rooms[room]):
            rooms[room]=node
            return True
    return False
    
    
    pass

def solution():
    global visited,cows,rooms
    N,M =map(int,input().split())
    rooms=[-1]*(M+1) # 노드가 0 부터시작하므로 닿을수 없는값으로 초기화
    cows= [[] for _ in range(N)]
    
    for i in range(N):
        __,*room=map(int,input().split())
        cows[i]=room
    
    ans=0
    
    for i in range(N):
        visited = [False]*(N+1)
        if dfs(i):
            ans+=1
    print(ans)
    
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass