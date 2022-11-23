# 하샤드수

def solution(x):
    return x%sum(list(map(int,str(x))))==0 