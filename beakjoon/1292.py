# 쉽게 푸는 문제
import sys
input=sys.stdin.readline
def solution():
    A,B=map(int,input().split())
    sequence=[[i]*i for i in range(1,B+1)]
    sequence=sum(sequence,[])
    print(sum(sequence[A-1:B]))
    pass

if __name__ =="__main__":
    solution()
    