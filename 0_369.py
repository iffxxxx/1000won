# �Ӿ��̴� ģ����� 369������ �ϰ� �ֽ��ϴ�.
# 369������ 1���� ���ڸ� �ϳ��� ��� 3, 6, 9�� ���� ���ڴ� ���� ��� 3, 6, 9�� ������ŭ �ڼ��� ġ�� �����Դϴ�.
# �Ӿ��̰� ���ؾ��ϴ� ���� order�� �Ű������� �־��� ��, �Ӿ��̰� �ľ��� �ڼ� Ƚ���� return �ϵ��� solution �Լ��� �ϼ��غ�����.

def solution(order):
    answer = [i for i in str(order) if (i in '369')]
    return len(answer)


# def solution(order):
#     return sum(map(lambda x: str(order).count(str(x)), [3, 6, 9]))
# map() �Լ��� ����Ʈ [3, 6, 9] �� ��ҿ� lambda �Լ��� ������


print(solution(29423))