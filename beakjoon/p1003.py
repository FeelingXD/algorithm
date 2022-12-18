# 피보나치
for i in range(int(input())):
    a, b = 1, 0
    for j in range(int(input())):
        a, b = b, a+b
    print(a, b, sep=' ')
