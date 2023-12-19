#N과 M (2)
import sys
input =sys.stdin.readline
answer=[]
def back(idx,li):
    global M,N
    if len(li)==M:
        answer.append(li[:])
        return
    else:
        for i in range(idx,N+1):
            back(i+1,li+[i])
            
def solution():
    global N,M,answer
    N,M=map(int,input().split())
    back(1,[])
    for v in answer:
        print(*v)
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass