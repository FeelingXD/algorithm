# 숫자 카드 나누기

import numpy as np

def solution(arrayA, arrayB):
    answer = 0
    gcd_A=int(np.gcd.reduce(arrayA))
    gcd_B=int(np.gcd.reduce(arrayB))
    if not any((i%gcd_A==0 for i in arrayB)):
        answer=max(answer,gcd_A)
    if not any((i%gcd_B==0 for i in arrayA)):
        answer=max(answer,gcd_B)
    return answer