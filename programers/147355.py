# 크기가 작은 부분문자열
def solution(t, p):
    ran = len(p)
    candidate = []
    for i in range(len(t)):
        candidate.append(int(t[i:i+ran]))
        if i+ran == len(t):
            break
    return len([i for i in candidate if i <= int(p)])
