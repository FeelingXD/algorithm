#접미사 배열
import sys
input =sys.stdin.readline

def solution():
    word=input().strip()
    li=[word[i:] for i in range(len(word))]
    li.sort()
    for word in li:
        print(word)
    
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass