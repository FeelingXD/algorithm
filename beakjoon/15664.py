#N과 M (10)
import sys
input =sys.stdin.readline
answer=[]
numbers=[]
def back(li):
    global M,N,answer,visited
    if len(li)==N:
        if answer and li==answer[-1]:
            return
        answer.append(li)
        return
    else:
        prev=-1
        for i in range(len(numbers)):
            if li and li[-1] > numbers[i]:
                continue
            if not visited[i] and prev != numbers[i]:
                visited[i]=True
                prev=numbers[i]
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