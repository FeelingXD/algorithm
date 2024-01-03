# 통계학
import sys
from collections import defaultdict
input =sys.stdin.readline

def solution():
    '''
    1. 산술평균 : N개의 수들의 합을 N으로 나눈 값
    2. 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
    3. 최빈값 : N개의 수들 중 가장 많이 나타나는 값
    4. 범위 : N개의 수들 중 최댓값과 최솟값의 차이
    '''
    n=int(input())
    li=[int(input()) for _ in range(n)]
    li.sort()
    modes=[]
    dic=defaultdict(int)
    mode=0
    
    for v in li:
        dic[v]+=1
    mv=max(dic.values())
    for k,v in dic.items():
        if v==mv:
            modes.append(k)
            
    mode=modes[0] if len(modes)==1 else modes[1]


    print(round(sum(li)/n))
    print(li[(n//2)])
    print(mode)
    print(li[-1]-li[0])
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass