# ���ڿ� my_string�� ���� n�� �Ű������� �־��� ��,
# my_string�� ����ִ� �� ���ڸ� n��ŭ �ݺ��� ���ڿ��� return �ϵ��� solution �Լ��� �ϼ��غ�����.

def solution(my_string, n):
    answer = ''
    for i in my_string:
        answer += i * n
    return answer


# def solution(my_string, n):
#     return ''.join(i*n for i in my_string)

print(solution("hello", 3))