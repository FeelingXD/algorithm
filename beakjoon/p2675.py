test_case=int(input())
for i in range(test_case):
    case=list(map(str,input().split()))
    for k in range(len(case[1])):
            word = case[1]
            print(int(case[0])*word[k],end='')
    print()
