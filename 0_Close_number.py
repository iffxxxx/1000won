# ���� �迭 array�� ���� n�� �Ű������� �־��� ��, array�� ����ִ� ���� �� n�� ���� ����� ���� return �ϵ��� solution �Լ��� �ϼ����ּ���.

def solution(array, n):
    Minus = sorted([abs(i - n) for i in array])
    if n - Minus[0] in array:
        answer = n - Minus[0]
    else:
        answer = Minus[0] + n
    return answer


def solution(array, n):
    array.sort(key = lambda x : (abs(x-n), x-n))
    answer = array[0]
    return answer
# lambda == �� �ٷ� ǥ���ϴ� �͸� �Լ�
# array.sort(key=lambda x: (abs(x-n), x-n)) == array�� (abs(x-n), x-n) ������ �����ϴ� ��
# sort(key = lambda x : (x[0], x[1]))

# solution=lambda a,n:sorted(a,key=lambda x:(abs(x-n),x))[0]


print(solution([3, 10, 28], 20))