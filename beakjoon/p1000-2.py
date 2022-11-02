#  연산자 없는 덧셈 비트연산 사용


a , b  =map(int, input().split())
def shiftadd(a,b) :
    if b==0 :
        return a
    shiftxor = a^b
    shiftand = a&b 

    return shiftadd(shiftxor, shiftand << 1)
print(shiftadd(a,b))