# 트럭
import sys
from collections import deque
input = sys.stdin.readline


def solution():
    n,w,l=map(int,input().split())# n  트럭의 갯수, w 다리의 길이 l 최대하중
    truck_weight=deque(map(int,input().split()))
    bridge=deque([0 for _ in range(w)])
    time=0
    c_weight=0
    while bridge:
        time+=1
        c_weight-=bridge.popleft()
        if truck_weight:
            if truck_weight and c_weight+truck_weight[0]<=l:
                c_weight+=truck_weight[0]
                bridge.append(truck_weight.popleft())
            else:
                bridge.append(0)
    return time
    
    
    pass
if __name__ =="__main__":
    print(solution())
    pass