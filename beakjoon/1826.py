# 연료채우기
import sys
import heapq
from collections import deque
input = sys.stdin.readline
if __name__ == "__main__":
    station_heap = []
    line = []
    for _ in range(n := int(input())):
        line.append(tuple(map(int, input().split())))  # 주유소 거리 , 연료량
    line.sort()
    line = deque(line)
    t, current_fuel = map(int, input().split())
    line.append((t, 0))
    answer = 0
    while line:
        c_distance, fuel = line.popleft()  # 현재 주유소까지의 거리와, 보유 연료량
        if current_fuel < c_distance:
            while station_heap and current_fuel < c_distance:
                current_fuel += heapq.heappop(station_heap)*-1  # 연료량더하기
                answer += 1
            if not station_heap and current_fuel < c_distance:
                print(-1)
                exit()

        heapq.heappush(station_heap, (-fuel))
    print(answer)
    pass
