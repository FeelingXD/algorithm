# 맥주 마시면서 걸어가기
import sys
from collections import deque
input = sys.stdin.readline


def get_distance(s_pos, e_pos):
    s_x, s_y = s_pos
    e_x, e_y = e_pos
    return abs(s_x-e_x)+abs(s_y-e_y)


def enable_distance(distance):
    return distance <= 1000


def bfs(st_pos, end_pos, stores):
    if enable_distance(get_distance(st_pos, end_pos)):
        return "happy"
    q = deque()
    visited = set()
    q.append(st_pos)
    while q:
        pos = q.popleft()
        if enable_distance(get_distance(pos, end_pos)):
            return "happy"
        else:
            for store in stores:
                if enable_distance(get_distance(pos, store)) and store not in visited:
                    visited.add(store)
                    q.append(store)
    return "sad"  # 실패
    pass


if __name__ == "__main__":
    case = int(input())
    for _ in range(case):
        sc = int(input())
        stores = []
        sp = tuple(map(int, input().split()))
        for _ in range(sc):
            stores.append(tuple(map(int, input().split())))
        ep = tuple(map(int, input().split()))

        '''
            bfs 식 
        '''

        print(bfs(sp, ep, stores))
        pass
    pass
