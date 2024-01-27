# 나이트 투어
import sys
input =sys.stdin.readline
ROWS=COLOUMS=6
visited=[[False]*6 for _ in range(6)]
moves=[[2,1],[-2,1],[1,2],[1,-2],[-1,2],[-1,-2],[2,-1],[-2,-1]] # 나이트의 이동

def board_to_pos(word): # 체스보드 위치를 좌표로 변환
    x=ord(word[0])-ord('A')
    y=ROWS-int(word[1])
    return (y,x)
def validate_move(s_pos,t_pos): # 현재위치와 다음위치 비교
    global visited 
    cy,cx=s_pos
    for dy,dx in moves:
        ny,nx=cy+dy,cx+dx
        if 0<=ny<ROWS and 0<=nx<COLOUMS and not visited[ny][nx] and (ny,nx)==t_pos:
            visited[ny][nx]=True
            return True
    return False
    pass
def solution():
    global visited
    
    poses=[board_to_pos(input().strip()) for _ in range(36)]
    y,x=poses[0]
    
    
    for i in range(36):
        if not validate_move(poses[i],poses[(i+1)%36]):
            return False
    return True
    pass
if __name__=="__main__": # 실행되는 부분
    print("Valid") if solution() else print("Invalid")
    pass