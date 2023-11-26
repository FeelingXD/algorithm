# 색종이
import sys
from collections import defaultdict
input =sys.stdin.readline
MAX=1001
def solution():
    board=[[0]*MAX for _ in range(MAX)]
    dic=defaultdict(int)
    for c,_ in enumerate(range(n:=int(input())),1):
        x1,y1,w,h=map(int,input().split())
        for y in range(y1,min(y1+h,MAX)):
            for x in range(x1,min(x1+w,MAX)):
                board[y][x]=c
    for y in range(MAX):
        for x in range(MAX):
            dic[board[y][x]]+=1
    for i in range(1,n+1):
        print(dic[i])
    pass

if __name__=="__main__": # 실행되는 부분
    solution()
    pass