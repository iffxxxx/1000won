# �� �� ���� ��ǥ�� ���� ������ �迭  dots�� ������ ���� �Ű������� �־����ϴ�.
# [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
# �־��� �� ���� ���� �� ���� �̾��� ��, �� ������ ������ �Ǵ� ��찡 ������ 1�� ������ 0�� return �ϵ��� solution �Լ��� �ϼ��غ�����.

def gradiant(dotA, dotB):
    dx = dotB[0] - dotA[0]
    dy = dotB[1] - dotA[1]
    return dy / dx

def solution(dots):
    dots.sort(key = lambda x:x[0])
    a, b, c, d = dots

    d1 = gradiant(a, b)
    d2 = gradiant(c, d)

    if d1 == d2:
        return 1
    return 0

# ������ ���̽� - �׽�Ʈ���̽� 1, 10
# def solution(dots):
#     dots.sort()
#     print(dots)
#     if dots[2][0] - dots[0][0] == dots[3][0] - dots[1][0]:
#         if dots[2][1] - dots[0][1] == dots[3][1] - dots[1][1]:
#             return 1
#     return 0

print(solution([(0,0),(1,0),(3,3),(4,3)]))