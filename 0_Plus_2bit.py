# �������� �ǹ��ϴ� �� ���� ���ڿ� bin1�� bin2�� �Ű������� �־��� ��, �� �������� ���� return�ϵ��� solution �Լ��� �ϼ����ּ���.

def solution(bin1, bin2):
    bin3 = bin(int(bin1, 2) + int(bin2, 2))
    return bin3[2:]

print(solution("1001", 	"1111"))