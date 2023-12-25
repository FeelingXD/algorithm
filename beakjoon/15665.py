#N과 M (11)
import sys
input =sys.stdin.readline
answer=[]
numbers=[]
def back(li):
    global M,N,answer,visited
    if len(li)==N:
        answer.append(li)
        return
    else:
        for i in range(len(numbers)):
            back(li+[numbers[i]])
    pass
def solution():
    global M,N,numbers,visited
    M,N=map(int,input().split())
    numbers=sorted(list((set(map(int,input().split())))))
    visited=[False]*M
    back([])
    for v in answer:
        print(*v)
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass