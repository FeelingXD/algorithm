def sol_loop(s):
    for idx in range(len(s)) :
        if idx+2<=len(s) and s[idx]==s[idx+1]:
            del s[idx:idx+2]
def solution(s):
    s=list(s)
    while True:
        condition=True
        for idx in range(len(s)) :
            if idx+2<=len(s) and s[idx]==s[idx+1]:
                del s[idx:idx+2]
                condition=False
                continue
        if condition: break
    return 1 if s==[] else 0
print(solution('cdcd'))