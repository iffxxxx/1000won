# �Ӿ��̴� ����� ���� 7�� ���� �����մϴ�.
# ���� �迭 array�� �Ű������� �־��� ��, 7�� �� �� �� �ִ��� return �ϵ��� solution �Լ��� �ϼ��غ�����.

def solution(array):
    return sum([str(i).count("7") for i in array])


# def solution(array):
#     return str(array).count('7')

print(solution([7, 77, 17]))