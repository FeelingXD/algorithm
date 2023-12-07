# 테이블 해시 함수
from functools import reduce
def mod(i,data):
    return sum([v%i for v in data])
    
def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key=lambda x:(x[col-1],-x[0]))
    res=[]
    
    for i in range(row_begin-1,row_end):
        res.append(mod(i+1,data[i]))
    
    return reduce(lambda x,y:x^y,res,0)