# � �ڿ����� �������� �� ������ ������ ��������� �մϴ�.
# ���� n�� �Ű������� �־��� ��, n�� ��������� 1�� �ƴ϶�� 2�� return�ϵ��� solution �Լ��� �ϼ����ּ���.

def solution(n):
    return 1 if (n ** 0.5 == int(n ** 0.5)) else 2
    # return 1 if (n ** 0.5).is_integer() else 2
    # return 1 if (n ** 0.5) % 1 == 0 else 2

print(solution(144))