# 피보나치 수 2
import sys
input =sys.stdin.readline

def solution():
    n=int(input())
    one,two=0,1
    for _ in range(1,n):
        one,two=two,one+two
    print(two) if n else print(0)
    
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass