def solution(ingredient):
    stack = []
    answer = 0
    for item in ingredient:
        if not stack:
            stack.append(item)
        else:
            if item == 1 and len(stack) >= 3:
                if stack[-3:] == [1, 2, 3]:
                    answer += 1
                    stack.pop()
                    stack.pop()
                    stack.pop()
                    continue
            stack.append(item)
    return answer
