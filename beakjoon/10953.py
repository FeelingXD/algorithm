# A+B - 6 
import sys
input =sys.stdin.readline

def solution():
    for _ in range(int(input())):
        a,b=map(int,input().split(","))
        print(a+b)
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass