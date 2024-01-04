# 먹을 것인가 먹힐 것인가
import sys
input =sys.stdin.readline
def action():
    len_A,len_B=map(int,input().split())
    
    list_A=list(map(int,input().split())) # A 리스트
    list_B=sorted(list(map(int,input().split()))) # B 리스트
    ans=0
    
    for v in list_A:
        l=0
        r=len_B-1
        m_i=-1
        while l<=r and v>list_B[0]: # 2진 탐색
            mid=(l+r)//2
            if v>list_B[mid]:
                m_i=mid
                l=mid+1
            else:
                r=mid-1
        ans+= m_i+1
    print(ans) 
        
    

    
    pass
def solution():
    for _ in range(int(input())):
        action()
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass