# 홀수
import sys
input=sys.stdin.readline

def solution():
    pass
if __name__ =="__main__":
    li=[]
    for _ in range(7):
        v=int(input())
        if v%2:
            li.append(v)
    if li:
        print(sum(li))
        print(min(li))
    else:
        print(-1)
    pass