# 세탁소 사장 동혁
import sys

input = sys.stdin.readline

coins=[25,10,5,1]
def get_coins(price):
    ans=[]
    for coin in coins:
        v,price=divmod(price,coin)
        ans.append(v)
    return ans
    pass

def solution():
    for _ in range(case:=int(input())):
        print(*get_coins(int(input())))
    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
