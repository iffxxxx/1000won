# ���� n�� �Ű������� �־��� ��, n�� ����� ������������ ���� �迭�� return�ϵ��� solution �Լ��� �ϼ����ּ���.

def solution(n):
    return [i for i in range(1, n + 1) if n % i == 0]


# def solution(n):
#     return list(filter(lambda v: n % v == 0, [i for i in range(1, n//2+1)])) + [n]
# ����� Ư¡ �� ���������� �ι�° ���Ҵ� ������ ������ 2/1�� ���ų� �ƴ� �۴�

print(solution(24))