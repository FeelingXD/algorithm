#치즈버거 만들기
import sys
input =sys.stdin.readline

def solution():
    # 패티 -치즈 - 패티 순으로 쌓여야 함
    
    p,c=map(int,input().split())
    print(2*p-1 if c>=p else 2*c+1)
    
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass