# 3x ���� ������� 3�� ������ ���ڶ�� �����ϱ� ������ 3�� ����� ���� 3�� ������� �ʽ��ϴ�.
# 3x ���� ������� ���ڴ� ������ �����ϴ�.

def solution(n):
    answer = 0
    for i in range(n):
        answer += 1
        while (answer % 3 == 0 or '3' in str(answer)):
            answer += 1
    return answer

print(solution(9))