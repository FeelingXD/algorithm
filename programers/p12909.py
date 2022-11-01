#올바른괄호


def solution(s):
    sum=0
    for i in s:
        if sum<0: 
            return False
        if i =='(':
            sum+=1
        else :
            sum-=1
    return True if sum==0 else False