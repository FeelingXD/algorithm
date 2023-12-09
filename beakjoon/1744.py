# 수 묶기
import sys
input =sys.stdin.readline


def solution():
    plus=[]
    minus=[]
    res=0
    for _ in range(n:=int(input())):
        v=int(input())
        if v>1:
            plus.append(v)
        elif v<=0:
            minus.append(v)
        else:
            res+=1
    plus.sort(reverse=True)
    minus.sort()
    
    # 양수
    for i in range(0,len(plus),2):
        if i+1>=len(plus): # 인덱스 초과
            res+=plus[i]
        else:
            res+=plus[i]*plus[i+1]
    #음수
    for i in range(0,len(minus),2):
        if i+1 >= len(minus):
            res+=minus[i]
        else:
            res+= (minus[i] * minus[i+1])
    print(res)
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass
#-2 -1 0 1 2 3