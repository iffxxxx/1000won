# ������ ��� �迭 array�� ���� n�� �Ű������� �־��� ��,
# array�� n�� �� �� �ִ� ���� return �ϵ��� solution �Լ��� �ϼ��غ�����.

def solution(array, n):
    answer = [i for i in array if i == n]
    return len(answer)

# def solution(array, n):
#     return sum(1 for x in array if x == n)


# def solution(array, n):
#     return array.count(n)

print(solution([1, 1, 2, 3, 4, 5], 1))