# 조합 0의 개수
import sys
input=sys.stdin.readline

def count_number(n,k):
    cnt=0
    while k<=n:
        cnt+=n//k
        n=n//k
    return cnt
        
    pass

def solution():
    N,M=map(int,input().split())
    
    count_two = count_number(N,2)-count_number(M,2) - count_number(N-M,2)
    count_five = count_number(N,5)-count_number(M,5) - count_number(N-M,5)
    
    print(min(count_two,count_five))# 둘중 승수가 작은경우
    
    pass

if __name__ == "__main__":
    solution()
    pass