# 카약과 강풍
import sys
input =sys.stdin.readline

def solution():
    N,S,R=map(int,input().split())
    
    broken_t=list(map(int,input().split()))
    reserve_t=list(map(int,input().split()))
    
    n_broken_t=set(broken_t)-set(reserve_t)
    n_reserve_t=set(reserve_t)-set(broken_t)
    
    answer=0
    n_broken_t=sorted(list(n_broken_t))
    for t in n_broken_t:
        if t-1 in n_reserve_t:
            n_reserve_t.remove(t-1)
        elif t+1 in n_reserve_t:
            n_reserve_t.remove(t+1)
        else:
            answer+=1
           
    print(answer)
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass