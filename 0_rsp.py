# ������ 2 ������ 0 ���� 5�� ǥ���մϴ�.
# ���� ���� ���� ���� ������� ��Ÿ�� ���ڿ� rsp�� �Ű������� �־��� ��, rsp�� ����� ���� ���� ���� ��� �̱�� ��츦 ������� ��Ÿ�� ���ڿ��� return�ϵ��� solution �Լ��� �ϼ��غ�����.

def solution(rsp):
    answer = ''
    rsp_win = {'2':'0', '0':'5', '5':'2'}
    for i in rsp:
        answer += rsp_win[i]
    return answer
    # return ''.join(rsp_win[i] for i in rsp)


# def solution(rsp):
#     return rsp.translate(str.maketrans('025', '502'))
# str.maketrans = ù���� �μ��� �ι�° �μ��� �� ���ڸ� ����
# translate = �� ���ڸ� �����Ǵ� ���ڷ� ġȯ�ϴ� ���

print(solution("205"))