# ����� a, e, i, o, u �ټ� ���� ���ĺ��� �������� �з��մϴ�.
# ���ڿ� my_string�� �Ű������� �־��� �� ������ ������ ���ڿ��� return�ϵ��� solution �Լ��� �ϼ����ּ���.

def solution(my_string):
    answer = my_string.translate({ord(letter) : None for letter in 'aeiou'})
    return answer


# def solution(my_string):
#     return ''.join([i for i in my_string if not (i in 'aeiou')])


print(solution('bus'))