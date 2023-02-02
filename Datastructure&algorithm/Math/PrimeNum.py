import math


def isPrime(num):
    if num == 2 or num == 3:
        return True
    if num == 1 or num % 2 == 0 or num % 3 == 0:
        return False
    else:
        for i in range(5, int(math.sqrt(num))+1, 2):
            if num % i == 0:
                return False
    return True


def Factorization(num):
    tmp = num
    answer = []
    if num <= 1:
        print("소인수 분해 불가 수 입니다.")
        return
    while (num % 2 == 0):
        answer.append(2)
        num /= 2

    for i in range(3, tmp, 2):
        if num <= 1:
            break
        if isPrime(i):
            while (num % i == 0):
                answer.append(i)
                num //= i

    if answer == []:
        answer.append(tmp)
    return answer


print("🐍 File: Math/Primenum.py | Line: 33 | undefined ~ Factorization(55)",
      Factorization(65))
