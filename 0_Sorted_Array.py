# 문자열 my_string이 매개변수로 주어질 때, my_string 안에 있는 숫자만 골라 오름차순 정렬한 리스트를 return 하도록 solution 함수를 작성해보세요.

def solution(my_string):
    answer = sorted([int(i) for i in my_string if (i in '0123456789')])
    return answer


# def solution(my_string):
#     return sorted([int(c) for c in my_string if c.isdigit()])
# str.isdigit() == 문자열이 '숫자'로만 이루어져있는지 확인하는 함수


print(solution("hi12392"))