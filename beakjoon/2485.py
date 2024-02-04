# 가로수
import sys
import math
sys.setrecursionlimit(10**6)
input =sys.stdin.readline

def multiple_gcd(arr:list,idx:int)->int:
    if idx==len(arr)-1:
        return arr[idx]
    
    a = arr[idx]
    b = multiple_gcd(arr,idx+1)
    return math.gcd(a,b)
    
    pass
def solution():
    ans=0
    
    trees=[int(input()) for _ in range(int(input()))]
    tree_interval=list(map(lambda x,y:y-x,trees[:-1],trees[1:]))
    
    gcd=multiple_gcd(tree_interval,0)
    ans=sum(v//gcd-1 for v in tree_interval)
    print(ans)
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass