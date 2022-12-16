#더 맵게
from heapq import *
def solution(scoville:list, K):
    answer=0
    heapify(scoville)
    while len(scoville)>=2 and scoville[0]<K:
        Fst = heappop(scoville)
        Snd = heappop(scoville)
        heappush(scoville,Fst+Snd*2)
        answer+=1
    if scoville[0]<K:
        return -1    
    return answer