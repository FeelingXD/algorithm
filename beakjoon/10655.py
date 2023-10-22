# 마라톤
from math import inf
import sys
input = sys.stdin.readline


def get_distance(x1, y1, x2, y2):
    return abs(x2-x1)+abs(y2-y1)


if __name__ == "__main__":
    case = int(input())
    check_points = [list(map(int, input().split())) for _ in range(case)]
    dist = [0]
    for i in range(case-1):
        dist.append(get_distance(*check_points[i], *check_points[i+1]))
    total = sum(dist)  # 원래의 최종값
    answer = total
    for i in range(1, case-1):  # 처음과 마지막은 건너뛸수없음
        tmp_dist = total-(dist[i]+dist[i+1])+get_distance(*
                                                          check_points[i-1], *check_points[i+1])
        answer = min(answer, tmp_dist)
    print(answer)
    pass
