# 정수 n이 매개변수로 주어질 때, n의 약수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.

def solution(n):
    return [i for i in range(1, n + 1) if n % i == 0]


# def solution(n):
#     return list(filter(lambda v: n % v == 0, [i for i in range(1, n//2+1)])) + [n]
# 약수의 특징 상 마지막에서 두번째 원소는 마지막 원소의 2/1과 같거나 아님 작다

print(solution(24))