# ���ڿ� �迭 strlist�� �Ű������� �־����ϴ�.
# strlist �� ������ ���̸� ���� �迭�� retrun�ϵ��� solution �Լ��� �ϼ����ּ���.

def solution(strlist):
    answer = []
    for i in strlist:
        answer.append(len(i))
    return answer


# def solution(strlist):
#     return [len(str) for str in strlist]