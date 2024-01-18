# 모바일 광고 입찰
import sys
input =sys.stdin.readline

def solution():
    
    N,K=map(int,input().split())
    diff_fee=[]
    
    for _ in range(N):
        current_fee, screen_price =map(int,input().split())
        diff_fee.append(screen_price-current_fee)
    diff_fee.sort()
    print(max(0,diff_fee[K-1]))
    
    
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass