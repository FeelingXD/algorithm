import sys
input =sys.stdin.readline


def solution():
    K=int(input())
    sizes=[2**i for i in range(21)]
    cnt=0
    
    for v in sizes:
        if v>=K:
            min_size=v
            break
        
    tmp=min_size
    if K!=min_size:
        while K:
            tmp//=2
            if K>=tmp:
                K-=tmp
                cnt+=1
            else:
                cnt+=1
    print(min_size,cnt)     
        
    
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass