#-2진수

import sys
input =sys.stdin.readline

def solution():
    n=int(input())
    ans=''
    if n==0:
        ans=0
    else:
        while n:
            if n%(-2): # 나머지가있는경우
                ans ='1' +ans
                n=n//-2+1
            else:
                ans='0'+ans
                n=n//-2
    print(ans)
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass