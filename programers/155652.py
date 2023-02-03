# 둘만의 암호
def solution(s, skip, index):
    answer = []
    skipN = [ord(skip[i]) for i in range(len(skip))]
    for c in s:
        for _ in range(index):
            c = chr(ord(c)+1)
            while c in skip:
                c = chr(ord(c)+1)
            if c > 'z':
                c = 'a'
            while c in skip:
                c = chr(ord(c)+1)
        answer.append(c)
    return ''.join(answer)
