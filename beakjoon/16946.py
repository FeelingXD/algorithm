# 벽 부수고 이동하기 4
import sys
from collections import deque
moves=[(0,1),(0,-1),(1,0),(-1,0)]
input =sys.stdin.readline
PATH='0'
WALL='1'
group_area={}
group_number=1

def draw_board(rows):
    return [input().strip() for _ in range(rows)]

def mark_board():
    global group_number,rows,coloums,group_area
    
    for y in range(rows):
        for x in range(coloums):
            if board[y][x]==PATH and not marked_group_number[y][x]:
                group_area[group_number]=bfs(y,x)
                group_number+=1

def bfs(y,x):
    global visited,group_number
    q=deque()
    q.append((y,x))
    
    visited[y][x]=True
    cnt=1
    
    while q:
        cy,cx=q.popleft()
        marked_group_number[cy][cx]=group_number
        
        for dy,dx in moves:
            ny,nx=cy+dy,cx+dx
            
            if 0<=ny<rows and 0<=nx<coloums and not visited[ny][nx] and board[ny][nx]==PATH:
                q.append((ny,nx))
                visited[ny][nx]=True
                cnt+=1
    return cnt
            
    
    pass
def calculate_able(y,x): # yx에서 이동가능한 그룹과 그결과
    data=set()
    cnt=1 
    
    for dy,dx in moves:
        ny,nx=y+dy,x+dx
        if 0<=ny<rows and 0<=nx<coloums and board[ny][nx]==PATH:
            data.add(marked_group_number[ny][nx])
    
    for value in data:
        cnt+=group_area[value]
    
    return cnt%10

def solution():
    
    global visited,group_number,marked_group_number,ans,board,rows,coloums
    
    rows,coloums=map(int,input().split())
    
    # init value
    visited=[[False]*coloums for _ in range(rows)]
    marked_group_number=[[0]*coloums for _ in range(rows)]
    ans=[[0]*coloums for _ in range(rows)]
    
    #draw board
    board= draw_board(rows)
    
    #mark board    
    mark_board()
    
    
    #real solution
    for y in range(rows):
        for x in range(coloums):
            if board[y][x]==WALL: # 벽일때 깨고 갈수잇는경우 구하기
                ans[y][x]=calculate_able(y,x)
    
    #print
    for line in ans:
        print(''.join(map(str,line)))
    
    
    
    pass

if __name__=="__main__": # 실행되는 부분
    solution()
    pass


