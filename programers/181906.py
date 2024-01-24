# 접두사인지 확인하기
def solution(my_string, is_prefix):
    return 1 if  is_prefix in my_string and my_string.index(is_prefix)==0 else 0