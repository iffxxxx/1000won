# ���ڿ� my_string�� �Ű������� �־��� ��, my_string �ȿ� �ִ� ���ڸ� ��� �������� ������ ����Ʈ�� return �ϵ��� solution �Լ��� �ۼ��غ�����.

def solution(my_string):
    answer = sorted([int(i) for i in my_string if (i in '0123456789')])
    return answer


# def solution(my_string):
#     return sorted([int(c) for c in my_string if c.isdigit()])
# str.isdigit() == ���ڿ��� '����'�θ� �̷�����ִ��� Ȯ���ϴ� �Լ�


print(solution("hi12392"))