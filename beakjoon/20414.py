# MVP 다이아몬드 (Normal)
import sys
input =sys.stdin.readline


def solution():
    rank="BSGPD" # 등급
    n=int(input())
    prices=list(map(int,input().split()))
    prices=[[s,e-1] for s,e in zip([0]+prices[:-1],prices)]
    MVP={k:v for k,v in zip(list(rank),prices)}

    MVP["D"]=[D:=prices[-1][1]+1,D*10]
    
    records=input().strip()
    tmp=[0]*n
    for i in range(len(records)):
        if i==0 or records[i]=="D": # 시작 인덱스 혹은 다이이아등급일경우
            tmp[i]=MVP[records[i]][1]
            continue
        if tmp[i-1]<MVP[records[i]][1]: # 문제 없는경우
            tmp[i]=MVP[records[i]][1]-tmp[i-1]

        elif tmp[i-1] > MVP[records[i]][1]:
            tmp[i]=0
            tmp[i-1]=MVP[records[i]][1]
            for j in range(i-1,-1,-1):
                # 과금 기준이 맞지않음 돌아가며 검산
                mvp_rank=records[j]
                if tmp[j]+tmp[j-1] < MVP[mvp_rank][0]: #두달의 합이 최솟값보다 커야함 
                    tmp[j-1]=MVP[mvp_rank][0]-tmp[j]
                elif tmp[j]+tmp[j-1] > MVP[mvp_rank][1]:# 두달의 합이 최대값보다 작아야함
                    tmp[j-1]=MVP[mvp_rank][1]-tmp[j]
                else:
                    break
    ans=0
    for v in tmp:
        ans+=min(MVP["D"][0],v)
    print(ans)
    
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass