# PROGRAMMERS-962 �༺�� �ҽ����� ���ֺ���� �Ӿ��̴� �ܰ��༺�� �� �����Ϸ��� �մϴ�. ���ĺ��� ��� �迭 spell�� �ܰ�� ���� dic�� �Ű������� �־����ϴ�. spell�� ��� ���ĺ��� �ѹ����� ��� ����� �ܾ dic�� �����Ѵٸ� 1, �������� �ʴ´ٸ� 2�� return�ϵ��� solution �Լ��� �ϼ����ּ���.

def solution(spell, dic):
    for i in dic:
        if sorted((set(spell))) == sorted(set(i)):
            return 1
    return 2


# def solution(spell, dic):
#     spell = set(spell)
#     for s in dic:
#         if not spell-set(s):
#             return 1
#     return 2

print(solution(["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo"]))