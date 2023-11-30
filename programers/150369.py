# 택배 배달과 수거하기 
def solution(cap, n, deliveries, pickups):
    answer = 0
    deliveries=deliveries[::-1]
    pickups=pickups[::-1]
    to_pick=0
    to_delivery=0
    
    for i in range(len(deliveries)):
        to_pick+=pickups[i]
        to_delivery+=deliveries[i]
        
        while to_pick>0 or to_delivery>0:
            to_pick-=cap
            to_delivery-=cap
            answer+=(n-i)*2
    return answer