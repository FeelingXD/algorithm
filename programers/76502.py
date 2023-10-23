# 괄호 회전하기
dic = {'{': '}', '[': ']', '(': ')'}
OPEN = ('(', '{', '[')
CLOSE = (')', '}', ']')
ERROR = False


def check(s):
    stack = []
    for c in s:
        if not stack:
            if c in OPEN:
                stack.append(c)
            else:
                return False
        else:
            if c in OPEN:
                stack.append(c)
            else:
                if dic.get(stack[-1], ERROR) == c:
                    stack.pop()
                else:
                    return False
    return True if not stack else False
    pass


def solution(s):
    answer = 0
    for i in range(len(s)):
        if check(s[i:]+s[:i]):
            answer += 1
    return answer
    pass


print(solution("[](){}"))
print(solution("}]()[{"))
