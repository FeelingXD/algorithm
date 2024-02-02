# 팰린드롬
import sys
input =sys.stdin.readline

def is_palindrome(word):
    return word == word[::-1]
    pass
def solution():
    for _ in range(int(input())): # case
        words=[]
        ans=0
        for _ in range(int(input())):
            words.append(input().strip()) # 단어 추가
        
        for i in range(len(words)):
            for j in range(len(words)):
                if i==j:
                    continue
                if is_palindrome(words[i]+words[j]):
                    ans=words[i]+words[j]  
                    break
            if ans:
                break
        print(ans)
        
        
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass

