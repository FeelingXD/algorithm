# Scholarship (장학금)
import sys
input =sys.stdin.readline

def solution():
    scores=[int(input()) for _ in range(int(input()))]
    ans="None"
    if ts:=set(scores) and 3 in set(scores):
        # 미가 하나라도 있는경우
        pass
    elif ts:=set(scores) and len(set(scores))==1 and 5 in set(scores):
        # 전체 성적이 5점인경우 개인 장학금
        ans="Named"  
    elif sum(scores)/len(scores)>=4.5:
        ans="High"
    else:
        ans="Common"
    
    print(ans)
    
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass