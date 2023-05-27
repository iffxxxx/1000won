# ���� �迭 num_list�� ���� n�� �Ű������� �־����ϴ�. num_list�� ���� ����� ���� 2���� �迭�� �ٲ� return�ϵ��� solution �Լ��� �ϼ����ּ���.
# num_list�� [1, 2, 3, 4, 5, 6, 7, 8] �� ���̰� 8�̰� n�� 2�̹Ƿ� num_list�� 2 * 4 �迭�� ������ ���� �����մϴ�.
# 2�������� �ٲ� ������ num_list�� ���ҵ��� �տ������� n���� ���� 2���� �迭�� �����մϴ�.

def solution(num_list, n):
    answer = []
    for i in range(len(num_list) // n):
        row = []
        for j in range(n):
            row.append(num_list.pop(0))
        answer.append(row)
    return answer


# def solution(num_list, n):
#     answer = []
#     for i in range(0, len(num_list), n):
#         answer.append(num_list[i:i+n])
#     return answer

print(solution([1, 2, 3, 4, 5, 6, 7, 8], 2))

