# �Ӿ��̴� ������ ģ���鿡�� �������ַ��� �մϴ�. ������ ��� �ٸ��� ������ϴ�.
# �Ӿ��̰� ���� �ִ� ������ ���� balls�� ģ���鿡�� ������ �� ���� ���� share�� �Ű������� �־��� ��,
# balls���� ���� �� share���� ������ ���� ������ ��� ����� ���� return �ϴ� solution �Լ��� �ϼ����ּ���.

def pac(number):
    j = 1
    for i in range(1, number + 1):
        j *= i
    return j

def solution(balls, share):
    answer = pac(balls) / (pac(balls - share) * pac(share))
    return int(answer)


# import math

# def solution(balls, share):
#     return math.comb(balls, share)

print(solution(3, 2))