# 중앙이동 알고리즘
import sys

input = sys.stdin.readline

def get_fact_num(n):
    res=2
    for i in range(n):
        res+=2**i
    return res

def solution():
    n=int(input())
    num=get_fact_num(n)
    print(num**2)
    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
