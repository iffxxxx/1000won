# �Ӿ��̴� ���α׷��ӽ��� �α����Ϸ��� �մϴ�.
# �Ӿ��̰� �Է��� ���̵�� �н����尡 ��� �迭 id_pw�� ȸ������ ������ ��� 2���� �迭 db�� �־��� ��,
# ������ ���� �α��� ����, ���п� ���� �޽����� return�ϵ��� solution �Լ��� �ϼ����ּ���.

# ���̵�� ��й�ȣ�� ��� ��ġ�ϴ� ȸ�������� ������ "login"�� return�մϴ�.
# �α����� �������� �� ���̵� ��ġ�ϴ� ȸ���� ���ٸ� ��fail����,
# ���̵�� ��ġ������ ��й�ȣ�� ��ġ�ϴ� ȸ���� ���ٸ� ��wrong pw���� return �մϴ�.

def solution(id_pw, db):
    for i, p in db:
        if i == id_pw[0]:
            if p == id_pw[1]:
                return "login"
            else:
                return "wrong pw"
    return 'fail'


# Solution 2
# def solution(id_pw, db):
#     if db_pw := dict(db).get(id_pw[0]):
#         return "login" if db_pw == id_pw[1] else "wrong pw"
#     return "fail"

print(solution(["meosseugi", "1234"], [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]))