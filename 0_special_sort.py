# ���� n�� �������� n�� ����� ������ �����Ϸ��� �մϴ�. �̶� n���κ����� �Ÿ��� ���ٸ� �� ū ���� �տ� ������ ��ġ�մϴ�. 
# ������ ��� �迭 numlist�� ���� n�� �־��� �� numlist�� ���Ҹ� n���κ��� ����� ������� ������ �迭�� return�ϵ��� solution �Լ��� �ϼ����ּ���.

def solution(numlist, n):
    answer = sorted([i - n for i in numlist], key = lambda x : [abs(x), -x])
    print([i - n for i in numlist])
    return [n + i for i in answer]

print(solution([1, 2, 3, 4, 5, 6], 4))