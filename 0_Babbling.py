# �Ӿ��̴� �¾ �� 6���� �� ��ī�� ������ �ֽ��ϴ�.
# ��ī�� ���� "aya", "ye", "woo", "ma" �� ���� ������ �ִ� �� ���� ����� ������(�̾� ����) �����ۿ� ���� ���մϴ�.
# ���ڿ� �迭 babbling�� �Ű������� �־��� ��, �Ӿ����� ��ī�� ������ �� �ִ� �ܾ��� ������ return�ϵ��� solution �Լ��� �ϼ����ּ���.

def solution(babbling):
    answer = 0
    form = ["aya", "ye", "woo", "ma"]
    for j in babbling:
        for i in form:
            j = j.replace(i, "1")
        if j.replace("1", '') == '':
            answer += 1
    return answer


# Solution 2 --- re.complie, match
# import re

# def solution(babbling):
#     regex = re.compile('^(aya|ye|woo|ma)+$')
#     cnt=0
#     for e in babbling:
#         if regex.match(e):
#             cnt+=1
#     return cnt


print(solution(["aya", "yee", "u", "maa", "wyeoo"]))

