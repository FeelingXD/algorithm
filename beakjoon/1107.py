# 리모컨
import sys
input =sys.stdin.readline

def solution():
    target=int(input())
    len_error_btn=int(input())
    err_btns=[]
    if len_error_btn:
        err_btns=list(map(str, input().strip()))
    
    # 기본답 100 채널에서 +- 로만 이동하는경우
    ans=abs(target-100)
    
    #상한선
    for i in range(target,target+(ans+1)):
        c_target=str(i)
        if not(set(err_btns) & set(c_target)):
            ans=min(ans,len(c_target)+abs(int(c_target)-target))
            break
    #하한선
    for i in range(target,target-(ans+1),-1):
        c_target=str(i)
        if not(set(err_btns) & set(c_target)):
            ans=min(ans,len(c_target)+abs(int(c_target)-target))
            break
    
    print(ans)
    
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass