# 피로도 
import sys
input =sys.stdin.readline
DAY=24
def solution():
    A,B,C,M=map(int,input().split())
    c_fatigue=0
    answer=0
    for _ in range(DAY):
        if c_fatigue+A <= M:
            c_fatigue+=A
            answer+=B
        else:
            c_fatigue= max(0,c_fatigue-C)
    print(answer)
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass