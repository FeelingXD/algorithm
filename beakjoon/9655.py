# 돌 게임 1
import sys
input =sys.stdin.readline

def solution():
    n=int(input())
    return "CY" if n%4 in (0,2) else "SK"
    pass
if __name__=="__main__": # 실행되는 부분
    print(solution())
    pass