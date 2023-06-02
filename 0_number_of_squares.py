# 어떤 자연수를 제곱했을 때 나오는 정수를 제곱수라고 합니다.
# 정수 n이 매개변수로 주어질 때, n이 제곱수라면 1을 아니라면 2를 return하도록 solution 함수를 완성해주세요.

def solution(n):
    return 1 if (n ** 0.5 == int(n ** 0.5)) else 2
    # return 1 if (n ** 0.5).is_integer() else 2
    # return 1 if (n ** 0.5) % 1 == 0 else 2

print(solution(144))