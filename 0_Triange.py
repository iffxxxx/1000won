# ���� �� ���� �ﰢ���� ����� ���ؼ��� ������ ���� ������ �����ؾ� �մϴ�.
# ���� �� ���� ���̴� �ٸ� �� ���� ������ �պ��� �۾ƾ� �մϴ�.
# �ﰢ���� �� ���� ���̰� ��� �迭 sides�� �Ű������� �־����ϴ�.
# �� ������ �ﰢ���� ���� �� �ִٸ� 1, ���� �� ���ٸ� 2�� return�ϵ��� solution �Լ��� �ϼ����ּ���.

def solution(sides):
    sides.sort()
    answer = sides[2] < sides[0] + sides[1]
    return 2 - int(answer)


# def solution(sides):
#     return 1 if max(sides) < (sum(sides) - max(sides)) else 2

print(solution([199, 72, 222]))