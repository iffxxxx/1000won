# �Ӿ��̳� ���ڰ��Դ� ���ڸ� ���� �������� �߶� �ݴϴ�.
# ���ڸ� �������� ����� �� n�� �Ű������� �־��� ��,
# n���� �ֹ��� ���ڸ� ������ �ʰ� ��� ���� ���� ���� ������ �Ծ�� �Ѵٸ� �ּ� �� ���� ���Ѿ� �ϴ����� return �ϵ��� solution �Լ��� �ϼ��غ�����.

def solution(n):
    if n % 6 == 0:
        answer = n//6
    else:
        for i in range(1, 100):
            if 6*i % n == 0:
                break
        answer = i
    return answer

# def solution(n):
#     answer = 1
#     while 6 * answer % n:   # 1 == True
#         answer += 1
#     return answer

print(solution(4))