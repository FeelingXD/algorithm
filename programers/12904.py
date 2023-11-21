# 가장 긴 펠린드롬
def isPalindrome(x):
    if x==x[::-1]:
        return True
    return False
def solution(word):
    answer = 0

    for s in range(len(word)):
        for e in range(s+1,len(word)+1):
            if len(word[s:e])>answer and isPalindrome(word[s:e]):
                answer=len(word[s:e])
                

    return answer