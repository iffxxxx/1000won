# �ֺ��� �־��� �� �߿��� ���� ���� ������ ���� �ǹ��մϴ�. 
# ���� �迭 array�� �Ű������� �־��� ��, �ֺ��� return �ϵ��� solution �Լ��� �ϼ��غ�����. �ֺ��� ���� ���� -1�� return �մϴ�.

def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            # print(set(array))
            # print(i, a)
            array.remove(a)
        if i == 0:
            return a
    return -1

print(solution([1, 1, 1, 2, 2, 3]))