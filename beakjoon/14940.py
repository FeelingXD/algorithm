# 쉬운 최단거리
import sys
from collections import deque
input =sys.stdin.readline
moves=[(0,1),(0,-1),(1,0),(-1,0)]
def find_target(board):
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x]==2:
                return (y,x)

def draw_board(n):
    board=[]
    for y in range(n):
        board.append(list(map(int,input().split())))
    return board

def bfs(board,ty,tx):
    
    bfs_board=[[-1]*len(board[0]) for _ in range(len(board))]
    
    visited=[[False]*len(board[0]) for _ in range(len(board))]
    
    q=deque()
    visited[ty][tx]=True
    bfs_board[ty][tx]=0
    
    q.append((ty,tx))
    while q:
        cy,cx=q.popleft()
        
        for move in moves:
            dy,dx=move
            ny,nx=dy+cy,dx+cx
            if 0<=ny<len(board) and 0<=nx<len(board[0]) and board[ny][nx]!=0 and not visited[ny][nx]:
                visited[ny][nx]=True
                bfs_board[ny][nx]=bfs_board[cy][cx]+1
                q.append((ny,nx))
    
    for y in range(len(bfs_board)):
        for x in range(len(bfs_board[0])):
            if board[y][x]==0:
                bfs_board[y][x]=0
    
    
    for y in range(len(bfs_board)):
        print(*bfs_board[y])      
                
                
        
    
def solution():
    n,m=map(int,input().split())
    board = draw_board(n)
    ty,tx=find_target(board)
    bfs(board,ty,tx)
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass