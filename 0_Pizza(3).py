# �Ӿ��̳� ���ڰ��Դ� ���ڸ� �� �������� �� �������� ���ϴ� ���� ���� �߶��ݴϴ�.
# ���� ���� �� slice�� ���ڸ� �Դ� ����� �� n�� �Ű������� �־��� ��, n���� ����� �ּ� �� ���� �̻� ���ڸ� �������� �ּ� �� ���� ���ڸ� ���Ѿ� �ϴ����� return �ϵ��� solution �Լ��� �ϼ��غ�����.

def solution(slice, n):
    a = n % slice > 0
    answer = n // slice + a
    return answer

# def solution(slice, n):
#     return ((n - 1) // slice) + 1

print(solution(5, 7))