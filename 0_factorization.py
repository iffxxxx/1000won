# ���μ����ض� � ���� �Ҽ����� ������ ǥ���ϴ� ���Դϴ�.
# ���� ��� 12�� ���μ� �����ϸ� 2 * 2 * 3 ���� ��Ÿ�� �� �ֽ��ϴ�. ���� 12�� ���μ��� 2�� 3�Դϴ�.
# �ڿ��� n�� �Ű������� �־��� �� n�� ���μ��� ������������ ���� �迭�� return�ϵ��� solution �Լ��� �ϼ����ּ���.

def solution(n):
    minority = [i for i in range(2, n + 1) if (n % i == 0)]
    answer  = []
    for j in minority:
        while n % j == 0:
            answer.append(j)
            n /= j
    return sorted(list(set(answer)))

# def solution(n):
#     minority = [i for i in range(2, n + 1) if (n % i == 0)]
#     answer  = []
#     for j in minority:
#         while n % j == 0:
#             if j not in answer:
#                 answer.append(j)
#             n /= j
#     return answer

print(solution(24))