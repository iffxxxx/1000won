# �Ҽ��� �Ʒ� ���ڰ� ��ӵ��� �ʰ� ���Ѱ��� �Ҽ��� ���ѼҼ���� �մϴ�. �м��� �Ҽ��� ��ĥ �� ���ѼҼ��� ��Ÿ�� �� �ִ� �м����� �Ǻ��Ϸ��� �մϴ�. ���ѼҼ��� �Ǳ� ���� �м��� ������ ������ �����ϴ�.

# ���м��� ��Ÿ������ ��, �и��� ���μ��� 2�� 5�� �����ؾ� �մϴ�.
# �� ���� a�� b�� �Ű������� �־��� ��, a/b�� ���ѼҼ��̸� 1��, ���ѼҼ���� 2�� return�ϵ��� solution �Լ��� �ϼ����ּ���.


from math import gcd

def solution(a, b):
    b //= gcd(a, b)
    while b % 2 == 0:
        b //= 2
    while b % 5 == 0:
        b //= 5
    return 1 if b == 1 else 2


# ������ ���̽�
# def solution(a, b):
#     answer = []
#     ab_minority = [i for i in range(2, b + 1) if a % i == 0 and b % i == 0]
#     b_minority = [i for i in range(2, b + 1) if b % i == 0]
    
#     for j in b_minority:
#         while b % j == 0:
#             answer.append(j)
#             b /= j

#     for m in ab_minority:
#         while a % m == 0:
#             answer.remove(m)
#             a /= m
#     return 1 if set(answer) | {2, 5} == {2, 5} else 2

print(solution(3, 6))