# ���ڿ� s�� �Ű������� �־����ϴ�.
# s���� �� ���� �����ϴ� ���ڸ� ���� ������ ������ ���ڿ��� return �ϵ��� solution �Լ��� �ϼ��غ�����.
# �� ���� �����ϴ� ���ڰ� ���� ��� �� ���ڿ��� return �մϴ�.

def solution(s):
    answer = ''
    my_string = sorted(list(s))
    for i in my_string:
        if my_string.count(i) == 1:
            answer += i
    return answer


# def solution(s):
#     return ''.join(sorted([i for i in set(s) if (s.count(i) == 1)]))
# set�� ���ؼ� for������ �ߺ��Ǵ� ���ڸ� �ϳ��� ������ -> �ߺ� ��ȸ�� ���δ�

print(solution("abcabcadc"))