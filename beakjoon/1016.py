# 제곱ㄴㄴ수
import sys
input =sys.stdin.readline

def solution():
    MIN,MAX=map(int,input().split())
    num=[True]*(MAX-MIN+1)
    
    for i in range(2, int(MAX**(1/2))+1):
        tmp=i**2
        while tmp<=MAX:
            start_idx=MIN//tmp*tmp
            for j in range(start_idx,MAX+1,tmp):
                if j<MIN:
                    continue
                num[j-MIN]=False if num[j-MIN] else None
            tmp*=i
    print(num.count(True))
    
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass