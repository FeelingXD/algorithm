import sys
input =sys.stdin.readline

def solution():
    n=int(input())
    li=list(map(int,input().split()))
    l,r=0,len(li)-1
    cur=float('inf')
    answer=cur
    while l<r:
        if (tmp:=(li[l]+li[r]))==0:
            return [li[l],li[r]]
        else:
            if abs(tmp)<cur:
                cur=abs(tmp)
                answer=[li[l],li[r]]
            if tmp>0:
                r-=1
            else:
                l+=1
    return answer
    pass
if __name__=="__main__": # 실행되는 부분
    res=solution()
    print(*res)
    pass