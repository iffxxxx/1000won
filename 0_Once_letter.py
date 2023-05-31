# 문자열 s가 매개변수로 주어집니다.
# s에서 한 번만 등장하는 문자를 사전 순으로 정렬한 문자열을 return 하도록 solution 함수를 완성해보세요.
# 한 번만 등장하는 문자가 없을 경우 빈 문자열을 return 합니다.

def solution(s):
    answer = ''
    my_string = sorted(list(s))
    for i in my_string:
        if my_string.count(i) == 1:
            answer += i
    return answer


# def solution(s):
#     return ''.join(sorted([i for i in set(s) if (s.count(i) == 1)]))
# set를 통해서 for문에서 중복되는 문자를 하나로 통합함 -> 중복 조회를 줄인다

print(solution("abcabcadc"))