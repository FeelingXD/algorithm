# 괄호 회전하기
dic = {'{': '}', '[': ']', '(': ')'}
OPEN = ('(', '{', '[')
CLOSE = (')', '}', ']')


def check(s):
    stack = []
    for c in s:
        if not stack and c in OPEN:
            stack.append(c)
        else:
            if not stack and c not in OPEN:
                return False
            elif stack and c in CLOSE and dic[stack[-1]] == c:
                stack.pop()
            elif stack and c in OPEN:
                stack.append(c)
            elif stack and c in CLOSE:
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
