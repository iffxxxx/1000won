# �Ӿ��̳� ���ڰ��Դ� ���ڸ� �ϰ� �������� �߶� �ݴϴ�. 
# ���ڸ� �������� ����� �� n�� �־��� ��, ��� ����� ���ڸ� �� ���� �̻� �Ա� ���� �ʿ��� ������ ���� return �ϴ� solution �Լ��� �ϼ��غ�����.

def solution(n):
    a = (n % 7) > 0
    answer = n//7 + a
    return answer


# def solution(n):
#     return (n - 1) // 7 + 1

print(solution(16))