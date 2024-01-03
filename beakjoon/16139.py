#인간-컴퓨터 상호작용
import sys
input =sys.stdin.readline

def solution():
    word=input().strip()
    for i in range(int(input())):
        c,s,e=map(str,input().split())
        print(word[int(s):int(e)+1].count(c))
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass