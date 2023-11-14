# 펠린드롬 만들기
import sys
from collections import Counter
input=sys.stdin.readline
FAIL="I\'m Sorry Hansoo"

def solution():
    word=input().strip()
    word_counter=Counter(word)
    
    if len(word)%2: # 단어길이가 홀수일떄
        if 1!=list(map(lambda x: x%2 ,word_counter.values())).count(1):
            return FAIL
        tmp=[]
        wildcard=""
        for c,v in word_counter.items():
            if v%2:
                wildcard=c
            for _ in range(v//2):
                tmp.append(c)
        tmp.sort()
        return ''.join(tmp)+wildcard+''.join(tmp[::-1])
    
    else: #짝수일때
        if len(s:=set(map(lambda x: x%2 ,word_counter.values())))>1 or 1 in s:
            return FAIL
        tmp=[]
        for c,v in word_counter.items():
            for _ in range(v//2):
                tmp.append(c)
        tmp.sort()
        return ''.join(tmp+tmp[::-1])
    
    pass

if __name__=="__main__":
    print(solution())
    pass

