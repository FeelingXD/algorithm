# 3진법 뒤집기
def convertion(n: int, b: int):
    answer = ''
    if n >= b:
        while n >= b:
            k, x = divmod(n, b)
            answer += str(x)
            n = k
        answer += str(k)
    else:
        answer += str(n)
    return answer[::-1]


def solution(n):
    answer = 0
    for i, v in enumerate(convertion(n, 3)):
        if v != 0:
            answer += int(v)*3**i
    return answer


convertion(1, 3)
print("🐍 File: programers/#test.py | Line: 19 | undefined ~ convertion(1,3)", convertion(1, 3))
