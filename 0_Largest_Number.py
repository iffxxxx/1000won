# ���� �迭 array�� �Ű������� �־��� ��, ���� ū ���� �� ���� �ε����� ���� �迭�� return �ϵ��� solution �Լ��� �ϼ��غ�����.

def solution(array):
    return [sorted(array)[-1], array.index(sorted(array)[-1])]


# def solution(array):
#     return [max(array), array.index(max(array))]
# max�Լ��� �־���

print(solution([9, 10, 11, 8]))