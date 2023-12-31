# 기타레슨
import sys
input =sys.stdin.readline

def solution():
    N,M=map(int,input().split())
    li=list(map(int,input().split()))
    l=0
    max_n=0
    r=1e9
    answer=float('inf')
    while l<r:
        cnt=1
        mid=(l+r)//2+1
        tmp=0
        max_n=0
        for v in li:
            if cnt >M:
                break
            
            if tmp+v<=mid:
                tmp+=v
            else:
                max_n=max(max_n,tmp)
                cnt+=1
                tmp=v
        max_n=max(max_n,tmp)
        
        if  M<cnt:
            l=mid+1
        else:
            if M>=cnt:
                answer=min(answer,max_n)

            r=mid-1
    print(answer)
    
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass