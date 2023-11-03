# 수리공 항승
import sys
input = sys.stdin.readline

if __name__=="__main__":
    N,L=map(int,input().split())
    if L==1000:
        print(1)
        exit()
    pipe=[False]*1001
    answer=0
    check_list=sorted(list(map(int,input().split())))
    for check in check_list:
        if not pipe[check]:
            for j in range(check,min(check+L,1001)):
                pipe[j]=True
            answer+=1
    print(answer)
    
    
    
    
    pass
