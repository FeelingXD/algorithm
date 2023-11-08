# 차집합
import sys
input = sys.stdin.readline



if __name__ == "__main__":  # 문제를 푸는 영역
    n,m=map(int,input().split())
    a=set(map(int,input().split()))
    b=set(map(int,input().split()))
    
    if result:=a-b:
        print(len(result))
        result_li=sorted(list(result))
        print(*result_li)
    else:
        print(0)
    