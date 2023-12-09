#다음 순열
import sys
input =sys.stdin.readline

def solution():
    n=int(input())
    data=list(map(int,input().split()))
    p1=-1
    p2=-1
    for i in range(len(data)-1,0,-1): # 뒤에서부터 탐색 
        if data[i]>data[i-1]:
            p1=i-1 # 가장큰 피크 인덱스
        if p1!=-1: # 피크인덱스를 찾았다면 
            p2= data.index(min([i for i in data[p1+1:] if data[p1]<i]))
            data[p1],data[p2]=data[p2],data[p1]
            return data[:p1+1]+sorted(data[p1+1:]) 
    return [-1]
            
            
    
    pass
if __name__=="__main__": # 실행되는 부분
    print(*solution())
    pass
# 1 2 3 4
# 1 2 4 3
# 1 3 2 4
# 1 3 4 2