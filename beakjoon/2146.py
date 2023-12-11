# 다리 만들기
import sys
from collections import deque
input =sys.stdin.readline
moves=[(0,1),(0,-1),(-1,0),(1,0)]
LAND = 1
SEA = 0

def get_mindist(s): # s 시작
    q=deque()
    dist=[[-1]*n for _ in range(n)]
    
    for y in range(n):
        for x in range(n):
            if marked_board[y][x]==s:
                dist[y][x]=0
                q.append((y,x))
    
    while q:
        cy,cx=q.popleft()
        for move in moves:
            dy,dx=move
            ny,nx=cy+dy,dx+cx
            if 0<=ny<n and 0<=nx<n:
                if marked_board[ny][nx]!=s and marked_board[ny][nx]!=SEA:
                    return dist[cy][cx]
                if marked_board[ny][nx]==SEA and dist[ny][nx]==-1:
                    dist[ny][nx]=dist[cy][cx]+1
                    q.append((ny,nx))
    print_board(dist)
        

def mark_island(board):#mark island
    global n
    global visited
    global mark_num
    visited=[[False]*n for _ in range(n)]
    mark_num=1
    
    def mark_bfs(y,x):
        global mark_num
        mark_num+=1
        q=deque()
        q.append((y,x))
        
        while q:
            cy,cx=q.popleft()
            board[cy][cx]=mark_num
            for move in moves:
                dy,dx=move
                ny,nx=cy+dy,dx+cx
                if 0<=ny<n and 0<=nx<n and not visited[ny][nx] and board[ny][nx]==LAND:
                    visited[ny][nx]=True
                    q.append((ny,nx))
                    
    for y in range(n):
        for x in range(n):
            if board[y][x]==LAND and not visited[y][x]: # board 땅부분이고 방문하지 않았다면
                mark_bfs(y,x)
    
    return board      
    pass

def print_board(board): # debug
    for v in board:
        print(v)

def get_board():
    global n
    n=int(input())
    return  [list(map(int,input().split())) for _ in range(n)]
    

def solution():
    global marked_board
    
    board=get_board()
    marked_board=mark_island(board)
    ans=1e9
    for i in range(2,mark_num+1):
        ans=min(ans,get_mindist(i))
    print(ans)
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass