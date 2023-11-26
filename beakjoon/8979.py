# 올림픽
import sys
input =sys.stdin.readline

def solution():
    N,K=map(int,input().split())
    li=[]
    for _ in range(N):
        c,g,s,cu=map(int,input().split())
        li.append(([c,g,s,cu]))
    li.sort(key=lambda x:(-x[1],-x[2],-x[3]))
    c_rank=1
    same_rank=1
    tmp_score=0
    for C,g,s,c in li:
        if C==K:
            return c_rank if tmp_score==(g,s,c) or not tmp_score else c_rank+same_rank
        else:
            if not tmp_score:
                tmp_score=(g,s,c)
            elif (g,s,c)==tmp_score:
                same_rank+=1
            else:
                tmp_score=(g,s,c)
                c_rank+=same_rank
                same_rank=1
    
    pass

if __name__=="__main__": # 실행되는 부분
    print(solution())
    pass