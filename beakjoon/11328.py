#Strfy
import sys
from collections import Counter
input= sys.stdin.readline

POSSIBLE="Possible"
IMPOSSIBLE="Impossible"

if __name__=="__main__":
    for _ in range(case:=int(input())):
        a,b =map(str,input().split())
       
        print(POSSIBLE) if Counter(a)==Counter(b) else print(IMPOSSIBLE)
            
    pass