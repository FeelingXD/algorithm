# 킹
import sys
input =sys.stdin.readline
move={"R":(0,1),"L":(0,-1),"T":(-1,0),"B":(1,0),"RT":(-1,1),"LT":(-1,-1),"RB":(1,1),"LB":(1,-1)}
'''
y= 숫자 좌표
x= 문자 좌표
'''
def board_to_pos(word): # 체스보드 위치를 좌표로 변환
    x=ord(word[0])-ord('A')
    y=8-int(word[1])
    return (y,x)

def pos_to_board(pos): # 좌표를 체스보드 위치로 변환
    y,x=pos
    return chr(x+ord('A'))+str(8-y)

def unit_move(next_move):
    global k_pos, p_pos
    
    k_cy,k_cx=k_pos
    dy,dx=move[next_move]
    
    k_ny,k_nx=k_cy+dy,k_cx+dx
    if not (0<=k_ny<8 and 0<=k_nx<8): # 왕이 보드칸을 넘어가는 경우
        return
    elif (k_ny,k_nx)==p_pos: # 왕이 이동하는칸에 폰이 있는 경우
        p_cy,p_cx=p_pos
        p_ny,p_nx=dy+p_cy,dx+p_cx
        
        if not (0<=p_ny<8 and 0<=p_nx<8): # 폰이 보드칸을 넘어가는 경우
            return
        # 킹을 폰위치로 폰은 새로운위치로 이동
        k_pos=p_pos
        p_pos=(p_ny,p_nx)
    else:
        k_pos=(k_ny,k_nx)    
    
        

def solution():
    global k_pos, p_pos
    k_pos,p_pos,cases=map(str,input().split())
    
    k_pos=board_to_pos(k_pos)
    p_pos=board_to_pos(p_pos)
    
    for _ in range(int(cases)):
        unit_move(input().strip())
    
    print(pos_to_board(k_pos))
    print(pos_to_board(p_pos))
    
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass