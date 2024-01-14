# 슈퍼 소수
import sys
input =sys.stdin.readline

def aristo_stick():
    global aristo
    aristo = [False,False] + [True]*(318137-1)
    for i in range(2,318137):
        if aristo[i]:
            for j in range(2*i,len(aristo),i):
                aristo[j]=False
    global primes,super_primes
    primes=[]
    super_primes=[]
    for i in range(len(aristo)):
        if aristo[i]:
            primes.append(i)
    
    for v in primes:
        if v-1<=len(primes):
            super_primes.append(primes[v-1])
        
            
        
def solution():
    aristo_stick()
    for _ in range(int(input())):
        print(super_primes[int(input())-1])
if __name__=="__main__": # 실행되는 부분
    solution()
    pass