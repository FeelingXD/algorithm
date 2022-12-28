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
    return int(convertion(n, 3)[::-1], 3)
