# ��� ���� �Ӿ��̴� ����� ǥ��Ǿ��ִ� ���ڸ� ���� �ٲٷ��� �մϴ�.
# ���ڿ� numbers�� �Ű������� �־��� ��, numbers�� ������ �ٲ� return �ϵ��� solution �Լ��� �ϼ��� �ּ���.

# def solution(numbers):
#     list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
#     for i in list:
#         numbers = numbers.replace(i, str(list.index(i)))
#     return int(numbers)


def solution(numbers):
    dict = {'zero' : 0, 'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4, 'five' : 5, 'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9}
    for key, value in dict.items():
        numbers = numbers.replace(key, str(value))
    # Or
    for k in dict.keys():
        numbers = numbers.replace(k, dict[k])
    return numbers


print(solution("onetwothreefourfivesixseveneightnine"))