# i���丮�� (i!)�� 1���� i���� ������ ���� �ǹ��մϴ�. ������� 5! = 5 * 4 * 3 * 2 * 1 = 120 �Դϴ�.
# ���� n�� �־��� �� ���� ������ �����ϴ� ���� ū ���� i�� return �ϵ��� solution �Լ��� �ϼ����ּ���.

def solution(n):
    answer = 0
    for i in range(1, 11):
        n //= i
        if n <= i:
            answer = i
            break
    return answer


# from math import factorial

# def solution(n):
#     k = 10
#     while n < factorial(k):
#         k -= 1
#     return k

# def solution(n):
#     answer = 1
#     factorial = 1
#     while factorial <= n:
#         answer += 1
#         factorial = factorial * answer
#     answer -= 1
#     return answer

print(solution(1))