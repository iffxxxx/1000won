# ���� n�� �Ű������� �־��� ��, n�� ����� ������������ ���� �迭�� return�ϵ��� solution �Լ��� �ϼ����ּ���.

def solution(n):
    return [i for i in range(1, n + 1) if n % i == 0]

print(solution(24))