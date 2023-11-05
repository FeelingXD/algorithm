# 말이되고픈 원숭이
import sys
from collections import deque
WALL=1
PATH=0
input = sys.stdin.readline
knight_moves=[(2,-1),(2,1),(-1,2),(-1,-2),(-2,1),(-2,-1),(1,-2),(1,2)]
moves=[(0,1),(1,0),(-1,0),(0,-1)]


def get_board(W,H):
    board=[]
    for _ in range(H):
        board.append(list(map(int,input().split())))
    return board
    pass
def bfs(K,W,H):
    check=[[K+1]*W for _ in range(H)]
    
    q=deque()
    check[0][0]=0
    q.append((0,0,0))
    cnt=1
    while q:
        for _ in range(len(q)): # 현재 큐에 있는만큼만 순회
            y,x,k=q.popleft()
            if (y,x)==(H-1,W-1):
                return cnt-1
            
            if k<K: # 말 이동 카운트가 있을경우
                for move in knight_moves:
                    dy,dx=move
                    ny,nx=y+dy,x+dx
                    if 0<=ny<H and 0<=nx<W and k+1<check[ny][nx] and board[ny][nx]!=WALL:
                        q.append((ny,nx,k+1))
                        check[ny][nx]=k+1
                        pass
            for move in moves: # 없어도 4방향 이동가능
                dy,dx=move
                ny,nx=y+dy,x+dx
                if 0<=ny<H and 0<=nx<W and k<check[ny][nx] and board[ny][nx]!=WALL:
                    q.append((ny,nx,k))
                    check[ny][nx]=k
                    pass
        cnt+=1
    return -1
def solution():
    global board
    K=int(input())
    W,H=map(int,input().split())
    board= get_board(W,H)
    print(bfs(K,W,H))
    pass

if __name__ =="__main__":
    solution()
    pass
