# ���ڿ� my_string�� �Ű������� �־����ϴ�.
# my_string�� �Ųٷ� ������ ���ڿ��� return�ϵ��� solution �Լ��� �ϼ����ּ���.

def solution(my_string):
    answer = my_string[::-1]
    return answer


# def solution(my_string):
#     return ''.join(list(reversed(my_string)))


# def solution(my_string):
#     answer = ''
#     for i in range(len(my_string)-1, -1, -1) :
#         answer += my_string[i]
#     return answer

print(solution("jaron"))