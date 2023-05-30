# 문자열 my_string이 매개변수로 주어집니다.
# my_string에서 중복된 문자를 제거하고 하나의 문자만 남긴 문자열을 return하도록 solution 함수를 완성해주세요.

def solution(my_string):
    answer = ''
    for i in my_string:
        if i not in answer:
            answer += i
    return answer


# def solution(my_string):
#     return ''.join(dict.fromkeys(my_string))
# dict.fromkeys(iterable, value=None) == 지정된 키(key) 리스트나 반복 가능한(iterable) 객체를 기반으로 새로운 딕셔너리를 생성하는 역할

print(solution("people"))