# 용액 합성하기
import sys
input =sys.stdin.readline

def solution():
    n=int(input())
    li=list(map(int,input().split()))
    ans=10e9
    l,r=0,n-1
    while l<r:
        tmp=li[l]+li[r]
        if abs(tmp)<=abs(ans):
            ans=tmp
        if tmp>0:
            r-=1
        else:
            l+=1
    print(ans)    

    
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass