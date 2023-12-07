# 숫자 이어붙이기
import sys
import math
from collections import defaultdict
input =sys.stdin.readline
MOD=1_000_000_007

def dfs(s,e):
    global graph
    global scores
    
    visited=[False]* (len(scores)+1)
    stack=[]
    stack.append((s,scores[s]))
    visited[s]=True
    
    while stack:
        node,num=stack.pop()
        if node==e:
            return num
        else:
            for next_node in graph[node]:
                if not visited[next_node]:
                    visited[next_node]=True
                    new_num=scores[next_node]
                    l= int(math.log10(new_num))+1
                    stack.append((next_node,((num*10**l)%MOD+new_num%MOD)%MOD))

    pass
def solution():
    global scores
    global graph    
    N,Q=map(int,input().split()) # 집의개수, 철수가 놀이할 횟수
    numbers=list(map(int,input().split()))
    scores=defaultdict(int)
    graph=defaultdict(list)
    # score
    for i,v in enumerate(numbers,1):
        scores[i]=v
    
    # graph
    for _ in range(N-1):
        s,e=map(int,input().split())
        graph[s].append(e)
        graph[e].append(s)
    
    # game
    for _ in range(Q):
        s,e=map(int,input().split())
        print(dfs(s,e))
    
    
    
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass

