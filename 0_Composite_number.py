# ����� ������ �� �� �̻��� ���� �ռ������ �մϴ�.
# �ڿ��� n�� �Ű������� �־��� �� n������ �ռ����� ������ return�ϵ��� solution �Լ��� �ϼ����ּ���.

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


# def solution(n): # ��� ����� Ȯ���� �ʿ� ���� ��� ��� �����ٱ����� Ȯ���� ���
#     output = 0
#     for i in range(4, n + 1):
#         for j in range(2, int(i ** 0.5) + 1):
#             if i % j == 0:
#                 output += 1
#                 break
#     return output


# def solution(n):
#     return [i for i in range(2, n + 1) if not all(i % j for j in range(2, i))] # 0 = false �ռ����� 0�� ���� �� �ۿ� ����


print(solution(10))