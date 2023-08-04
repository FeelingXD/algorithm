# 큰수 만들기
def solution(number, k):
    stack = []
    for c in number:
        if not stack:
            stack.append(c)
        else:
            while k and stack and int(stack[-1]) < int(c):
                stack.pop()
                k -= 1
            stack.append(c)

    return ''.join(stack) if not k else ''.join(stack[:-k])  # k 가 소비되지않을경우
