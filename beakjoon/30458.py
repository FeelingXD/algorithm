#팰린드롬 애너그램
import sys
from collections import Counter
input = sys.stdin.readline

def solution():
    n=int(input()) # 길이
    li=list(input().strip())
    even =True if n%2==0 else False
    clue = Counter(li) if even else Counter(li[:n//2])+Counter(li[(n//2)+1:]) 
    for v in clue.values():
        if v%2:
            return 'No'
    return 'Yes'
    pass

if __name__=="__main__":
    print(solution())
    pass