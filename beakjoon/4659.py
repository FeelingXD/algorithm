#비밀번호 발음하기
import sys
import re
input = sys.stdin.readline
SUCCESS = "is acceptable."
FAIL ="is not acceptable."


def check(word):
    # 모음검사
    vowel_pattern = re.compile(r'[aeiou]')
    if not re.search(vowel_pattern,word):
        return False
    # 자음모음 3연속검사
    three_sequence =re.compile(r'[aeiou]{3}|[^aeiou]{3}')
    if re.search(three_sequence ,word):
        return False
    # ee , oo 를 제외한 연속 철자
    same_letter_twice = re.compile(r'([a-df-np-z])\1')
    if re.search(same_letter_twice,word):
        return False
    return True    
    pass
def success(word):
    return f"<{word}> "+SUCCESS
    pass
def fail(word):
    return f"<{word}> "+FAIL

def solution():
    
    while word:=input().strip():
        if word=="end":
            break
        print(success(word)) if check(word) else print(fail(word))  
    pass

if __name__ =="__main__":
    solution()
    pass