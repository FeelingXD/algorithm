# 수들의 합
import sys
input = sys.stdin.readline
'''
서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?

'''


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
    