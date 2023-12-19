#N과 M (3)
import sys
input =sys.stdin.readline
answer=[]
def back(li):
    global M,N
    if len(li)==M:
        answer.append(li[:])
        return
    else:
        for i in range(1,N+1):
            back(li+[i])
            
def solution():
    global N,M,answer
    N,M=map(int,input().split())
    back([])
    for v in answer:
        print(*v)
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass