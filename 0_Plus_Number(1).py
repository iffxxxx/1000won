# 문자열 my_string이 매개변수로 주어집니다. my_string안의 모든 자연수들의 합을 return하도록 solution 함수를 완성해주세요.

def solution(my_string):
    answer = sum([int(i) for i in my_string if (i.isdigit())])
    return answer

# isdecimal() == 주어진 문자열이 int형으로 변환이 가능한지 알아내는 함수
# isdigit() == 단일 글자가 '숫자' 모양으로 생겼으면 무조건 True를 반환하는 함수. 
# isnumeric() == 숫자값 표현에 해당하는 문자열까지 인정

print(solution("aAb1B2cC34oOp"))