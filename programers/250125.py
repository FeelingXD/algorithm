#[PCCE 기출문제] 9번 / 이웃한 칸
moves=[(0,1),(1,0),(-1,0),(0,-1)]
def solution(board, h, w):
    color=board[h][w]
    answer=0
    for move in moves:
        dy,dx=move
        ny,nx=h+dy,w+dx  
        if 0<=ny<len(board) and 0<=nx<len(board[0]):
            if color== board[ny][nx]:
                answer+=1
    return answer