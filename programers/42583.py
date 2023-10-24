# 다리를 지나는 트럭
from collections import deque


def solution(bridge_length, weight, truck_weight):
    time = 0
    current_weight = 0
    truck_weight = deque(truck_weight)
    bridge = deque([0 for _ in range(bridge_length)])
    while bridge:
        time += 1
        current_weight -= bridge.popleft()
        if truck_weight:
            if current_weight+truck_weight[0] <= weight:
                current_weight += truck_weight[0]
                bridge.append(truck_weight.popleft())
            else:
                bridge.append(0)
    return time
