# my_string�� "3 + 5"ó�� ���ڿ��� �� �����Դϴ�.
# ���ڿ� my_string�� �Ű������� �־��� ��, ������ ����� ���� return �ϴ� solution �Լ��� �ϼ����ּ���.

def solution(my_string):
    arr = my_string.split(" ")
    answer = int(my_string[0])
    for i in range(1, len(arr), 2):
        if arr[i] == "+":
            answer += int(arr[i + 1])
        elif arr[i] == '-':
                answer -= int(arr[i+1])
        else:
            continue
    return answer


# def solution(my_string):
#     return eval(my_string)
# eval() == ���ڿ��� ������ ������ִ� �Լ�

# def solution(my_string):
#     return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))
# - ���б�ȣ�� ���ڿ� ������ �ο�

print(solution("3 + 4 - 7 + 100"))