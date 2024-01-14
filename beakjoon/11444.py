# 피보나치 수 6
import sys
input =sys.stdin.readline
MOD=1_000_000_007
def mul(A, B):
    n = len(A)
    Z = [[0]*n for _ in range(n)]
    
    for row in range(n):
        for col in range(n):
            e = 0
            for i in range(n):
                e += A[row][i] * B[i][col]
            Z[row][col] = e % MOD
            
    return Z

def square(A, k):
    if k == 1:
        for x in range(len(A)):
            for y in range(len(A)):
                A[x][y] %= MOD
        return A
    
    tmp = square(A, k//2)
    if k % 2:
        return mul(mul(tmp, tmp), A)
    else:
        return mul(tmp, tmp)

def solution():
    global n
    n=int(input())
    fib_matrix = [[1, 1], [1, 0]]
    print(square(fib_matrix, n)[0][1])
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass