#x만큼 간격이 있는 n개의 숫자
def solution(x, n):
    return [x for x in range(x,x*n+1,x)] if x >0 else  [0]*n if x==0 else  [x for x in range(x,(x*n)-1,x)] 