# 정수 배열 numbers가 매개변수로 주어집니다.
# numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.

def solution(numbers):
    a = numbers.pop(numbers.index(max(numbers)))
    b = numbers.pop(numbers.index(max(numbers)))
    answer = a * b
    return answer

# pop()는 맨 마지막 요소를 출력, pop(n)은 n번째 요소 리턴


# def solution(numbers):
#     numbers.sort()
#     return numbers[-2] * numbers[-1]

# def solution(numbers):
#     numbers.sort(reverse=True)
#     return numbers[0]*numbers[1]

print(solution([1, 2, 3, 4, 5]))