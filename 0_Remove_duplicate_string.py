# ���ڿ� my_string�� �Ű������� �־����ϴ�.
# my_string���� �ߺ��� ���ڸ� �����ϰ� �ϳ��� ���ڸ� ���� ���ڿ��� return�ϵ��� solution �Լ��� �ϼ����ּ���.

def solution(my_string):
    answer = ''
    for i in my_string:
        if i not in answer:
            answer += i
    return answer


# def solution(my_string):
#     return ''.join(dict.fromkeys(my_string))
# dict.fromkeys(iterable, value=None) == ������ Ű(key) ����Ʈ�� �ݺ� ������(iterable) ��ü�� ������� ���ο� ��ųʸ��� �����ϴ� ����

print(solution("people"))