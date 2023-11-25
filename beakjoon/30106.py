#현이의 로봇 청소기
import sys
from collections import deque
input =sys.stdin.readline
moves=[(0,1),(1,0),(-1,0),(0,-1)]

def check(y1,x1,y2,x2):
    return K>=abs(board[y2][x2]-board[y1][x1])
    
    pass
def bfs(y,x):
    visited[y][x]=True
    
    q=deque()
    q.append((y,x))
    while q:
        cy,cx=q.popleft()
        for move in moves:
            dy,dx=move
            ny,nx=cy+dy,cx+dx
            if 0<=ny<N and 0<=nx<M and check(cy,cx,ny,nx) and not visited[ny][nx]:
                visited[ny][nx]=True
                q.append((ny,nx))
        
        
    pass

def solution():
    global N,M,K,board,visited
    N,M,K=map(int,input().split())
    board=[list(map(int,input().split())) for _ in range(N)]
    visited=[[False]*M for _ in range(N)]
    answer=0
    for y in range(N):
        for x in range(M):
            if not visited[y][x]:
                bfs(y,x)
                answer+=1
    
    print(answer)
    
    
    pass

if __name__=="__main__": # 실행되는 부분
    solution()
    pass