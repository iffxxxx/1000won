# ���ڿ� str1, str2�� �Ű������� �־����ϴ�.
# str1 �ȿ� str2�� �ִٸ� 1�� ���ٸ� 2�� return�ϵ��� solution �Լ��� �ϼ����ּ���.

def solution(str1, str2):
    for i, j in enumerate(str1):
        if j == str2[0]:
            if str1[i : i + len(str2)] == str2:
                    return 1
    return 2


# def solution(str1, str2):
#     return 1 if str2 in str1 else 2
#     return 1 + int(str2 not in str1)


print(solution("ab6CDE443fgh22iJKlmn1o", "6CD"))