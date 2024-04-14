# 진법 변환 2
import sys

input = sys.stdin.readline

def change_formation(n:int,formation:int):
    tmp=''
    while n:
        current_value =n%formation
        if 10<=current_value:
            tmp+=chr(current_value+55)
        else:
            tmp+=str(current_value)
        n//=formation
    return tmp[::-1]
def solution():
    res=change_formation(*map(int,input().split()))
    print(res)
    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
