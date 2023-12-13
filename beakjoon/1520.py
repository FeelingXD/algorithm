# 내리막길
import sys
sys.setrecursionlimit(10**9)
input =sys.stdin.readline
moves=[(0,-1),(0,1),(1,0),(-1,0)]
def validate(y,x,now):
    global row,col,graph
    return 0<=y<row and 0<=x<col and graph[y][x]<now
    pass
def dfs(y,x):
    global row,col
    if y==row-1 and x==col-1: # 목적지일 경우 탈출
        return 1
    if dp[y][x]==-1:
        dp[y][x]=0
        for move in moves:
            dy,dx=move
            ny,nx=y+dy,x+dx
            if validate(ny,nx,graph[y][x]):
                dp[y][x]+=dfs(ny,nx)
    return dp[y][x]
    pass

def solution():
    global row,col,graph,dp
    row,col=map(int,input().split())
    dp=[[-1]*col for _ in range(row)]
    graph=[list(map(int,input().split())) for _ in range(row)]
    print(dfs(0,0))
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass