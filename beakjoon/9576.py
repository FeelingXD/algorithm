# 책 나눠주기
import sys
input =sys.stdin.readline

def solution():
    for _ in range(case:=int(input())): # 테스트 케이스 반복
        N,M=map(int,input().split())
        book=[True]*(N+1)
        ranges=[]
        ans=0
        for _ in range(M):
            ranges.append(tuple(map(int,input().split())))
        
        ranges.sort(key=lambda x:x[1]) # 끝 값을 기준으로 정렬
        
        for st,end in ranges:
            for i in range(st,end+1):
                if book[i]:
                    book[i]=False
                    ans+=1
                    break
        print(ans)
                
            
        
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass