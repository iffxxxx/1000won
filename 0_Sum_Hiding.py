# ���ڿ� my_string�� �Ű������� �־����ϴ�. my_string�� �ҹ���, �빮��, �ڿ����θ� �����Ǿ��ֽ��ϴ�.
# my_string���� �ڿ������� ���� return�ϵ��� solution �Լ��� �ϼ����ּ���.

def solution(my_string):
    answer = ''
    for i in my_string:
        if i.isdigit():
            answer += i
        else:
            answer += " "
    num = answer.split(" ")
    return sum([int(i) for i in num if i.isdigit()])
# join() �޼���� ���ڿ��� ��ȯ�ϰ� ������ ���ڿ��� �������� �ʽ��ϴ�. 


# def solution(my_string):
#     s = ''.join(i if i.isdigit() else ' ' for i in my_string)
#     return sum(int(i) for i in s.split())
# split() = ����� ���͸� �����Ѵ�.


# import re
# def solution(my_string):
#     return sum(map(int,re.findall(r"[0-9]+",my_string)))
# map(int, ...) �Լ��� �־��� �Լ�(���⼭�� int)�� ����Ʈ�� �� ��ҿ� �����Ͽ� ���ο� ����Ʈ�� ����
# re.findall(r"[0-9]+", my_string)���� r"[0-9]+"�� 1�� �̻��� ���ӵ� ���ڸ� ��Ÿ���� ���� ǥ����


print(solution("aAb1B2cC34oOp"))