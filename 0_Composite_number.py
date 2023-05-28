# 약수의 개수가 세 개 이상인 수를 합성수라고 합니다.
# 자연수 n이 매개변수로 주어질 때 n이하의 합성수의 개수를 return하도록 solution 함수를 완성해주세요.

def solution(n):
    answer = n - 1
    for i in range(1, n + 1):
        num = 0
        for j in range(1, i):
            if i % j == 0:
                num += 1
        if num == 1:
            answer -= 1
    return answer


# def solution(n): # 모든 약수를 확인할 필요 없이 가운데 약수 제곱근까지만 확인한 경우
#     output = 0
#     for i in range(4, n + 1):
#         for j in range(2, int(i ** 0.5) + 1):
#             if i % j == 0:
#                 output += 1
#                 break
#     return output


# def solution(n):
#     return [i for i in range(2, n + 1) if not all(i % j for j in range(2, i))] # 0 = false 합성수는 0이 나올 수 밖에 없음


print(solution(10))