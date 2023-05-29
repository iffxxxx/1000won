# ���ڿ� "Z"�� �������� ���еǾ� ��� ���ڿ��� �־����ϴ�.
# ���ڿ��� �ִ� ���ڸ� ���ʴ�� ���Ϸ��� �մϴ�. �� �� "Z"�� ������ �ٷ� ���� ���ߴ� ���ڸ� ���ٴ� ���Դϴ�.
# ���ڿ� "Z"�� �̷���� ���ڿ� s�� �־��� ��, �Ӿ��̰� ���� ���� return �ϵ��� solution �Լ��� �ϼ��غ�����.

def solution(s):
    s = s.split()
    for i, j in enumerate(s):
        if j == 'Z':
            s.pop(i - 1)
    answer = sum([int(i) for i in s if (i.lstrip("-").isdigit())])
    return answer
# isdigit �� �������� False�� ����


# def solution(s):
#     answer = 0
#     for i in range(len(s := s.split(" "))):
#         answer += int(s[i]) if s[i] != "Z" else -int(s[i-1])
#     return answer
# :=�� �Ҵ� ǥ����(assignment expression) �Ǵ� walrus �����ڶ�� �Ҹ��� ǥ�����Դϴ�.
# �� �����ڴ� ������ ���� �Ҵ��ϰ�, ���ÿ� �Ҵ��� ���� ��ȯ


# def solution(s):
#     stack = []
#     for a in s.split():
#         if a != 'Z':
#             stack.append(int(a))
#         else:
#             if stack:
#                 stack.pop()
#     return sum(stack)
# if stack: == 'stack'�� ������� ���� ��� �ڵ� ��� ����
# stack�� LIFO(Last in First come) ���� ex. ���̽�ũ����, �����۽���


print(solution("-1 -2 -3 Z"))