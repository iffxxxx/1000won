# 문자열 my_string이 매개변수로 주어집니다. my_string은 소문자, 대문자, 자연수로만 구성되어있습니다.
# my_string안의 자연수들의 합을 return하도록 solution 함수를 완성해주세요.

def solution(my_string):
    answer = ''
    for i in my_string:
        if i.isdigit():
            answer += i
        else:
            answer += " "
    num = answer.split(" ")
    return sum([int(i) for i in num if i.isdigit()])
# join() 메서드는 문자열을 반환하고 기존의 문자열을 수정하지 않습니다. 


# def solution(my_string):
#     s = ''.join(i if i.isdigit() else ' ' for i in my_string)
#     return sum(int(i) for i in s.split())
# split() = 띄어쓰기와 엔터를 구분한다.


# import re
# def solution(my_string):
#     return sum(map(int,re.findall(r"[0-9]+",my_string)))
# map(int, ...) 함수는 주어진 함수(여기서는 int)를 리스트의 각 요소에 적용하여 새로운 리스트를 생성
# re.findall(r"[0-9]+", my_string)에서 r"[0-9]+"는 1개 이상의 연속된 숫자를 나타내는 정규 표현식


print(solution("aAb1B2cC34oOp"))