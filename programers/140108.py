# 문자열 나누기
def solution(s):
    answer = 0
    stack = []
    for a in s:
        if stack == []:
            stack.append(a)
        else:
            if stack[0] != a:
                stack.pop()
            else:
                stack.append(stack[0])
            if stack == []:
                answer += 1
    if stack != []:
        answer += 1
    return answer
