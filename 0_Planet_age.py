# ���ֿ����� �ϴ� �Ӿ��̴� ���� �������� PROGRAMMERS-962 �༺�� �ҽ����ϰ� �ƽ��ϴ�. �Ա��ɻ翡�� ���̸� ���ؾ� �ϴµ�, PROGRAMMERS-962 �༺������ ���̸� ���ĺ����� ���ϰ� �ֽ��ϴ�.
# a�� 0, b�� 1, c�� 2, ..., j�� 9�Դϴ�.
# ���� ��� 23���� cd, 51���� fb�� ǥ���մϴ�. ���� age�� �Ű������� �־��� �� PROGRAMMER-962�� ���̸� return�ϵ��� solution �Լ��� �ϼ����ּ���.

def solution(age):
    answer = ''
    Age = list(enumerate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']))
    for i in str(age):
        answer += (Age[int(i)][1])
    return answer


# def solution(age):
#     answer = ''
#     alpha = {'0':'a', '1':'b', '2':'c', '3':'d', '4':'e', '5':'f',
#             '6':'g', '7':'h', '8':'i', '9':'j'}
    
#     for i in str(age):
#         answer += (alpha[i])
#         answer = ''.join(alpha[i] for i in str(age))
#     return answer


# def solution(age):
#     return ''.join([chr(int(i)+97) for i in str(age)])

print(solution(23))