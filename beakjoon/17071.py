#숨바꼭질5

import sys
from collections import deque
input=sys.stdin.readline
MAX_NUM=500000

def solution():
    N, K = map(int, input().split())

    time = 1
    move = [[-1, -1] for _ in range(500001)]  
    move[N][0] = 0
    points = set([N])

    if N != K:
        while K < 500001:
            n_points = set()
            for subin in points:
                for nxt in (subin-1, subin+1, subin*2):
                    if -1 < nxt < 500001:
                        flag = time % 2
                        if move[nxt][flag] < 0:
                            move[nxt][flag] = time
                            n_points.add(nxt)

            points = n_points

            K += time
            if K < 500001:
                flag = time % 2
                
                if move[K][flag] > -1:
                    break           

                time += 1
    else:
        time = 0

    if K < 500001:
        print(time)
    else:
        print(-1)
        pass
if __name__=="__main__":
    solution()
    pass