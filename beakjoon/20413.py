# MVP 다이아몬드 (Easy)
import sys
input =sys.stdin.readline


def solution():
    rank="BSGPD" # 등급
    n=int(input())
    prices=list(map(int,input().split()))
    
    MVP={k:v-1 for k,v in zip(list(rank),prices)}
    MVP["D"]=prices[-1]
    
    records=input().strip()
    tmp=[]
    for i in range(len(records)):
        if i==0 or records[i]=="D":
            tmp+=[MVP[records[i]]]
        else:
            tmp+=[MVP[records[i]]-tmp[-1]]
    print(sum(tmp))              
    
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass