# ���� ��ҹ��ڷ� �̷���� ���ڿ� my_string�� �Ű������� �־��� ��,
# my_string�� ��� �ҹ��ڷ� �ٲٰ� ���ĺ� ������� ������ ���ڿ��� return �ϵ��� solution �Լ��� �ϼ��غ�����.

def solution(my_string):
    return ''.join(sorted([i for i in my_string.lower()]))
    # return ''.join(sorted(my_string.lower()))
    

# def solution(my_string):
#     answer = []
#     for i in my_string:
#         if ord(i) >= ord('A') and ord(i) <= ord('Z'):   # �빮�� �Ǻ� ord() == �����ڵ� ���� ��ȯ
#             answer.append(chr(ord(i)+32))               # �ҹ��� ��ȯ
#         else:
#             answer.append(i)
#     return ''.join(sorted(answer))

