# ���ڿ� my_string�� ���� num1, num2�� �Ű������� �־��� ��,
# my_string���� �ε��� num1�� �ε��� num2�� �ش��ϴ� ���ڸ� �ٲ� ���ڿ��� return �ϵ��� solution �Լ��� �ϼ��غ�����.

# def solution(my_string, num1, num2):
#     table = str.maketrans(my_string[num1] + my_string[num2], my_string[num2] + my_string[num1])
#     answer = my_string.translate(table)
#     return answer
# translate �Լ��� ����ϱ� ���ؼ��� skr.maketrans�� ����ؼ� ������ ��������Ѵ�.

def solution(my_string, num1, num2):
    my_list = list(my_string)
    my_list[num1], my_list[num2] = my_list[num2], my_list[num1]
    return ''.join(my_list)

print(solution("hello", 1, 2))