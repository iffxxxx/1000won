# �� ������ �Ӿ��̴� ���� �� ������ ������ ���� ��ȣ ü�踦 ����Ѵٴ� ���� �˾Ƴ½��ϴ�.
# ��ȣȭ�� ���ڿ� cipher�� �ְ�޽��ϴ�.
# �� ���ڿ����� code�� ��� ��° ���ڸ� ��¥ ��ȣ�Դϴ�.
# ���ڿ� cipher�� ���� code�� �Ű������� �־��� �� �ص��� ��ȣ ���ڿ��� return�ϵ��� solution �Լ��� �ϼ����ּ���.

def solution(cipher, code):
    answer = ""
    for i in range(code - 1, len(cipher), code):
        answer += cipher[i]
    return answer


# def solution(cipher, code):
#     answer = cipher[code-1::code]
#     return answer
# cipher[code-1::code] == cipher ���ڿ����� �ε����� code-1���� �����Ͽ� code ����(step)���� ���ڸ� �����ϴ� ���� �ǹ�

print(solution("pfqallllabwaoclk", 2))