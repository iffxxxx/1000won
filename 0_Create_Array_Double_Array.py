#정수 배열 numbers가 매개변수로 주어집니다. numbers의 각 원소에 두배한 원소를 가진 배열을 return하도록 solution 함수를 완성해주세요.

def solution(numbers):
    answer = [2 * i for i in numbers]
    return answer
# [표현식 for 항목 in 반복가능객체 if 조건문] 형태를 "리스트 컴프리헨션"이라고 한다.

print(solution([1, 2, 3, 4, 5]))