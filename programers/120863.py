# 다항식 더하기
def solution(polynomial) -> str:
    ans = ""
    polynomial = polynomial.replace(" ", "")
    nums = polynomial.split("+")
    x_nums = []
    static_nums = []
    for num in nums:
        if "x" in num:
            if len(num) == 1:
                x_nums.append(1)
            else:
                x_nums.append(int(num[:-1]))
        else:
            static_nums.append(int(num))
    if n := sum(x_nums):
        if n == 1:
            ans += "x"
        else:
            ans += f"{n}x"
    if n := sum(static_nums):
        if not n:
            if not ans:
                ans += "0"
        else:
            ans = ans + f" + {n}" if ans else f"{n}"
    return ans
