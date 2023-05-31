# 문자열 my_string과 정수 num1, num2가 매개변수로 주어질 때,
# my_string에서 인덱스 num1과 인덱스 num2에 해당하는 문자를 바꾼 문자열을 return 하도록 solution 함수를 완성해보세요.

# def solution(my_string, num1, num2):
#     table = str.maketrans(my_string[num1] + my_string[num2], my_string[num2] + my_string[num1])
#     answer = my_string.translate(table)
#     return answer
# translate 함수를 사용하기 위해서는 skr.maketrans를 사용해서 매핑을 시켜줘야한다.

def solution(my_string, num1, num2):
    my_list = list(my_string)
    my_list[num1], my_list[num2] = my_list[num2], my_list[num1]
    return ''.join(my_list)

print(solution("hello", 1, 2))