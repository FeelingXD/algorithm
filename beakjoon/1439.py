# 뒤집기
import sys
from collections import Counter
input =sys.stdin.readline

def solution():
    word= input().strip()
    greedy = Counter([word[0]] + [word[i] for i in range(1, len(word)) if word[i] != word[i - 1]])
    print(0 if len(greedy)==1 else min(greedy.values()))
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass