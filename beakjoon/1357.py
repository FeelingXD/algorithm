# 뒤집힌 덧셈
import sys
input =sys.stdin.readline

def rev(n)->int:
    return int(str(n)[::-1])
def solution():
    X,Y=map(int,input().split())
    print(rev(rev(X)+rev(Y)))
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass