#1, 2, 3 더하기 2
import sys
input =sys.stdin.readline
cnt=0
answer=[-1]
def back(li):
    global target,K,answer,cnt
    if sum(li)==target:
        cnt+=1
        if K==cnt:
            answer=li
            return
    for i in range(1,4):
        if sum(li)+i<=target:
            back(li+[i])
def solution():
    global target,K,answer
    target,K=map(int,input().split())
    back([])
    print('+'.join(map(str,answer)))
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass