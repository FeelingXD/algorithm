# 빛의경로 사이클
moves= [(0,1),(1,0),(0,-1),(-1,0)] # R,D,L,U
def move(y,x,d):
    global n,m
    dy,dx=moves[d]
    return (y+dy)%n,(x+dx)%m
    
def turn(d,node):
    global n,m
    if node =='R': # 우회전
        d=(d+1)%4
    elif node =='L': # 좌회전
        d=(d-1)%4
    return d  # S 일경우 직진이므로 변경 x  
    
def solution(grid):
    global n,m
    n,m= len(grid),len(grid[0])
    visited=[[[False]*4 for _ in range(m)] for _ in range(n)]
    answer = []
    for y in range(n):
        for x in range(m):
            for d in range(4):
                if not visited[y][x][d]:
                    cy,cx,cd= y,x,d
                    cnt=0
                    while not visited[cy][cx][cd]:
                        visited[cy][cx][cd]=True
                        cnt+=1
                        cy,cx=move(cy,cx,cd)
                        cd = turn(cd,grid[cy][cx])
                    answer.append(cnt)
    answer.sort()
    return answer
solution(["SSS", "LLL"])