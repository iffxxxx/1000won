# ���� �� ���� �ﰢ���� ����� ���ؼ��� ������ ���� ������ �����ؾ� �մϴ�.

# ���� �� ���� ���̴� �ٸ� �� ���� ������ �պ��� �۾ƾ� �մϴ�.
# �ﰢ���� �� ���� ���̰� ��� �迭 sides�� �Ű������� �־����ϴ�.
# ������ �� ���� �� �� �ִ� ������ ������ return�ϵ��� solution �Լ��� �ϼ����ּ���.

def solution(sides):
    answer = len([i for i in range(max(sides) - min(sides) + 1, sum(sides))])
    return answer

print(solution([3,6]))
