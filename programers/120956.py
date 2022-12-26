# 옹알이(1)
def solution(babbling):
    can_babel = {'a': 'aya', 'y': 'ye', 'w': 'woo', 'm': 'ma'}

    answer = 0
    for babble in babbling:
        ban = []
        build_str = ''
        while build_str in babble:
            # break point
            if '?' in build_str:
                break
            if build_str == babble:
                answer += 1
                break
            if babble[len(build_str)] in ban:
                break

            ban.append(babble[len(build_str)])
            build_str += can_babel.get(babble[len(build_str)], '?')

    return answer
