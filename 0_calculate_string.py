# my_string은 "3 + 5"처럼 문자열로 된 수식입니다.
# 문자열 my_string이 매개변수로 주어질 때, 수식을 계산한 값을 return 하는 solution 함수를 완성해주세요.

def solution(my_string):
    arr = my_string.split(" ")
    answer = int(my_string[0])
    for i in range(1, len(arr), 2):
        if arr[i] == "+":
            answer += int(arr[i + 1])
        elif arr[i] == '-':
                answer -= int(arr[i+1])
        else:
            continue
    return answer


# def solution(my_string):
#     return eval(my_string)
# eval() == 문자열의 수식을 계산해주는 함수

# def solution(my_string):
#     return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))
# - 수학기호를 숫자에 음수로 부여

print(solution("3 + 4 - 7 + 100"))