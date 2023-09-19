# 수열의 합
import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    # 합이 N 이며 , 최소 L개 이상으로  0이상의 정수인 연속수로 N 을표현할수있는지 검사
    N, L = map(int, input().split())
    '''
    nx = (x+1).....(x+i)/2 가우스 덧셈
    N= x+1......x+i//2    => N=
    x를 추출하여 시작점을 찾음
    '''
    for i in range(L, 101):  # 100 이상일경우 pass
        x = N - i * (i + 1) / 2
        if x % i == 0:
            x = int(x / i)
            if x >= -1:
                print(*list(range(x + 1, x + i + 1)))
                break
    else:
        print(-1)
        pass
