# �������̶� �� ���� ���ڸ� ������ ���Ͽ� ¦���� ��Ÿ�� ������ (a, b)�� ǥ���մϴ�.
# �ڿ��� n�� �Ű������� �־��� �� �� ������ ���� n�� �ڿ��� �������� ������ return�ϵ��� solution �Լ��� �ϼ����ּ���.

def solution(n):
    i = 1
    answer = []
    while i <= n:
        if n % i == 0:
            answer.append(i)
        i += 1
    return len(answer)

# def solution(n):
#     return len([number for number in range(1, n+1) if n%number == 0])

print(solution(20))