# 걷기
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    # x,y,w,s
    # x,y = 도착점 좌표
    # w: x 나 y 를 한칸 이동할때 걸리는시간
    # s: 대각이동 할때(x,y) 걸리는 시간
    x, y, w, s = map(int, input().split())
    gap = abs(x-y)  # 큰수에서 작은수를 뺀값
    diagnol = min(x, y)    # 대각 이동 가능한수
    move1 = (x+y)*w  # 평행이동만 하는경우

    if (x+y) % 2 == 0:  # 짝수일때
        move2 = max(x, y) * s
    else:
        move2 = (max(x, y)-1) * s+w
    move3 = min(x, y)*s+gap*w

    print(min(move1, move2, move3))
