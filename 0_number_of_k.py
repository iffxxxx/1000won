# 1���� 13������ ������, 1�� 1, 10, 11, 12, 13 �̷��� �� 6�� �����մϴ�.
# ���� i, j, k�� �Ű������� �־��� ��, i���� j���� k�� �� �� �����ϴ��� return �ϵ��� solution �Լ��� �ϼ����ּ���.

def solution(i, j, k):
    temp = [str(m) for m in range(i, j + 1)]
    answer = ''.join(temp)
    return len([i for i in answer if i == str(k)])


# def solution(i, j, k):
#     answer = sum([ str(i).count(str(k)) for i in range(i,j+1)])
#     return answer


# def solution(i, j, k):
#     return sum(map(lambda v: str(v).count(str(k)), range(i, j+1)))

# 0_369.py
# def solution(order):
#     return sum(map(lambda x: str(order).count(str(x)), [3, 6, 9]))
# map() �Լ��� ����Ʈ [3, 6, 9] �� ��ҿ� lambda �Լ��� ������


print(solution(1,13,1))