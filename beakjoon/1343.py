# 폴리오미노
import sys
input =sys.stdin.readline

def solution():
    word=input().strip().replace('XXXX','AAAA').replace('XX','BB')
    return -1 if word.count('X') else word
    pass

if __name__=="__main__": # 실행되는 부분
    print(solution())
    pass