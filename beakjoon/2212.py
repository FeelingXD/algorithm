# 센서
import sys
input =sys.stdin.readline
def solution():
    N=int(input())
    K=int(input())
    li=list(map(int,input().split()))
    li.sort()
    ranged=[]
    for i in range(0,N-1):
        ranged.append(li[i+1]-li[i])
    ranged.sort()
    print(sum(ranged[:N-K]))
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass