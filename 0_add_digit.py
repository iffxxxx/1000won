# ���� n�� �Ű������� �־��� �� n�� �� �ڸ� ������ ���� return�ϵ��� solution �Լ��� �ϼ����ּ���

def solution(n):
    return sum([int(i) for i in str(n)])


# def solution(n):
#     answer = 0
#     while n:
#         n, r = divmod(n, 10)
#         answer += r
#     return answer
# divmod() == �� ���� ���ڸ� ���ڷ� �޾�, ù�� ° ���ڸ� �ι� ° ���ڷ� ���� ��� �������� Ʃ��(tuple) ���·� ��ȯ

print(solution(1234))