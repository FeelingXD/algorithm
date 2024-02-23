# 도로와 신호등
import sys
from collections import deque

input = sys.stdin.readline


def solution():
    N, L = map(int, input().split())  # 신호등 개수 와 도로 길이
    traffic_lights = deque()
    t = current = 0
    for _ in range(N):
        traffic_lights.append(list(map(int, input().split())))

    next_light = traffic_lights.popleft()
    while current < L:
        if next_light and current == next_light[0]:
            while t % (next_light[1] + next_light[2]) < next_light[1]:
                t += 1
            next_light = traffic_lights.popleft() if traffic_lights else None

        current += 1
        t += 1
    print(t)

    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
