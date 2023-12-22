#N과 M (5)
import sys
input =sys.stdin.readline
answer=[]
numbers=[]
def back(li,):
    global M,N,answer,visited
    if len(li)==N:
        answer.append(li)
        return
    else:
        for i in range(len(numbers)):
            if not visited[i]:
                visited[i]=True
                back(li+[numbers[i]])
                visited[i]=False
    pass
def solution():
    global M,N,numbers,visited
    M,N=map(int,input().split())
    numbers=sorted(list(map(int,input().split())))
    visited=[False]*M
    back([])
    for v in answer:
        print(*v)
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass