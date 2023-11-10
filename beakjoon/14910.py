#오르막
import sys
input=sys.stdin.readline
from collections import deque
def solution():
    li=list(map(int,input().split()))
    tmp=li[0]
    for i in range(1,len(li)):
        if tmp>li[i]:
            print("Bad")
            exit()
        tmp=li[i]
    print("Good")

    pass
if __name__ =="__main__":
    solution()