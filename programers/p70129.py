# 이진 반복하기 
def solution(s):
    changes,zero_count=0, 0
    s=list(s)
    while not(len(s)==1):
        zero_count+=s.count('0')
        s=list(str(format(s.count('1'),'b')))
        changes+=1
    return [changes,zero_count]