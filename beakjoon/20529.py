# 가장 가까운 세 사람의 심리적 거리
import sys
from itertools import combinations
input =sys.stdin.readline

def psychological_range(a,b):
    return sum(1 for i in range(4) if a[i]!=b[i])
    pass
def get_range(a,b,c):
    return (psychological_range(a,b)+psychological_range(b,c)+psychological_range(a,c))
def solution():
    for _ in range(T:=int(input())):
        n=int(input())
        mbtis=tuple(input().split())
        ans=9999999
        if n>32:
            print(0)
        else: # brute
            for v in combinations(mbtis,3):
                ans=min(ans,get_range(*v))
            print(ans)
            
            
        
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass