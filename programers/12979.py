# 기지국 설치
def solution(n, stations, w):
    
    ans=0
    position=1
    station=0
    
    while position<=n:
        if station< len(stations) and stations[station]-w <= position:
            position = stations[station]+w+1
            station+=1
        else:
            print(f"설치 : {position}")
            position+=2*w+1
            ans+=1
    print(ans)        
    return ans
