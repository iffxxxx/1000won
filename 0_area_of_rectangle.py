# 2���� ��ǥ ��鿡 ���� ��� ������ ���簢���� �ֽ��ϴ�.
# ���簢�� �� �������� ��ǥ [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]�� ����ִ� �迭 dots�� �Ű������� �־��� ��,
# ���簢���� ���̸� return �ϵ��� solution �Լ��� �ϼ��غ�����.

def solution(dots):
    dots.sort()
    return (dots[3][0] - dots[0][0]) * (dots[3][1] - dots[0][1])


# def solution(dots):
#     return (max(dots)[0] - min(dots)[0])*(max(dots)[1] - min(dots)[1])

print(solution([[1, 1], [2, 1], [2, 2], [1, 2]]))