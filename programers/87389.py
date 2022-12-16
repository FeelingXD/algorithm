#나머지가 1이 되는 수 찾기
import math
def solution(n):
    for i in range(2,int(math.sqrt(n-1))+1 ):
        if n%i==1:
            return i
        
    return n-1
