# �� �迭�� �󸶳� �������� Ȯ���غ����� �մϴ�.
# ���ڿ� �迭 s1�� s2�� �־��� �� ���� ������ ������ return�ϵ��� solution �Լ��� �ϼ����ּ���.

def solution(s1, s2):
    answer = 0
    for i in s1:
        if i in s2:
            answer += 1
    return answer

# def solution(s1, s2):
#     return len(set(s1)&set(s2))
# s1&s2 != unsupported operand type(s) for &: 'list' and 'list'
# & �� ������ - ����Ʈ Ÿ���� ���� ������ �������� ���� - �������� ��ȯ�� �ʿ��ϴ�

print(solution(["a", "b", "c"], ["com", "b", "d", "p", "c"]))