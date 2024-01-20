# Y
import sys
from collections import defaultdict
input =sys.stdin.readline
MOD=10**9+7
def solution():
    '''
     
    $4$개의 정점과 
    $3$개의 간선을 가집니다.
    하나의 정점을 루트라고 부르며, 나머지 
    $3$개의 정점을 리프라고 부릅니다.
     
    $3$개의 간선은 각각의 리프와 루트를 연결합니다.
    '''
    n,m=map(int,input().split())
    edges=defaultdict(list)
    ans=0
    # edge 추가
    for _ in range(m):
        n1,n2=(map(int,input().split()))
        edges[n1].append(n2)
        edges[n2].append(n1)
    # 
    for value in edges.values():
        # value 는 현재 노드에대해 연결가능한 목록
        if (tmp:=len(value))>=3:
            ans+=tmp*(tmp-1)*(tmp-2)//6
    print(ans%MOD)
    
    pass
if __name__=="__main__": # 실행되는 부분
    
    solution()
    pass