# ���ڿ� my_string�� ���� letter�� �Ű������� �־����ϴ�.
# my_string���� letter�� ������ ���ڿ��� return�ϵ��� solution �Լ��� �ϼ����ּ���.

def solution(my_string, letter):
    answer = my_string.replace(letter, "")
    return answer

print(solution("abcdef", "f"))