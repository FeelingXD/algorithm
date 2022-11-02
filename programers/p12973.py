# 효율성 망 
# def solution(s):
#     s=list(s)
#     while True:
#         condition=True
#         for idx in range(len(s)) :
#             if idx+2<=len(s) and s[idx]==s[idx+1]:
#                 del s[idx:idx+2]
#                 condition=False
#                 continue
#         if condition: break
#     return 1 if s==[] else 0
# 시간복잡도 o(n^3)
def solution(s):
    stack = []
    for i in range(len(s)):
        if len(stack) == 0:
            stack.append(s[i])
        elif s[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(s[i])
    return 1 if len(stack)==0 else 0