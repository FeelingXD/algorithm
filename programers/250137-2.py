# [PCCP 기출문제] 1번- deque 풀이

from collections import deque
def solution(bandage, health, attacks):
    max_health=health
    c_t=0
    attacks=deque(attacks)
    while attacks and health>0:
        t,d=attacks.popleft()
        if not c_t:
            c_t=t    
            health-=d
            continue
        else:
            bt,bh,ah=bandage
            health+=(t-c_t-1)*bh
            health+=((t-c_t-1)//bt)*ah
            health=min(health,max_health)
        c_t=t
        health-=d
    return health if health >0 else -1 