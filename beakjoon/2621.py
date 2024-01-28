# 카드게임
import sys
from collections import defaultdict
input =sys.stdin.readline

def is_stair(li): # 계단식을 이루는지
    
    return len(li)==5 and all(li[i]+1==li[i+1] for i in range(len(li)-1))
    pass

def solution():
    cards=[tuple(map(lambda x,y: (x,int(y)),*(input().split())))[0] for _ in range(5)]
    color=set([card[0] for card in cards])  
    numbers=defaultdict(int) # number: count
    (None for x in [numbers.update({card[1]: numbers[card[1]] + 1}) for card in cards]) 
    stair_case=is_stair(sorted(numbers.keys()))
    
    MAX=max(numbers.keys()) # 자주사용되는 숫자의 최대값 저장
    ans=MAX+100 # 탑
    
    if len(color)==1 and len(set(numbers.keys()))==5 and stair_case: #스트레이트 플러쉬
        ans=max(MAX+900,ans)
    elif any(k>=4 for k in numbers.values()): # 포카드
        for k in numbers.keys():
            if numbers[k]>=4:
                ans=max(k+800,ans)    
    elif 3 in numbers.values() and 2 in numbers.values():# 풀하우스
        three =0
        two =0
        for k in numbers.keys():
            if three and two:
                 break
            elif not three and numbers[k]==3:
                 three=k
            elif not two and numbers[k]==2:
                two=k
        ans=max(700+three*10+two,ans)
    elif len(color)==1: # 플러쉬
        ans=max(600+MAX,ans)
    elif stair_case: #스트레이트
        ans=max(MAX+500,ans)
    elif 3 in numbers.values(): # 트리플
        for k in numbers.keys():
            if numbers[k]==3:
                ans=max(400+k,ans)
    elif [*numbers.values()].count(2)==2: # 투페어
        tmp=set()
        for k in numbers.keys():
            if len(tmp)==2:
                break
            elif numbers[k]==2:
                tmp.add(k)
        ans=max(max(tmp)*10+min(tmp)+300,ans)
    elif 2 in numbers.values(): # 원페어
        for k in numbers.keys():
            if numbers[k]==2:
                ans=max(k+200,ans)
                break
        pass
    
    print(ans)
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass
