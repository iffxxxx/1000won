# ���ڿ� my_string�� �Ű������� �־����ϴ�. my_string���� ��� �ڿ������� ���� return�ϵ��� solution �Լ��� �ϼ����ּ���.

def solution(my_string):
    answer = sum([int(i) for i in my_string if (i.isdigit())])
    return answer

# isdecimal() == �־��� ���ڿ��� int������ ��ȯ�� �������� �˾Ƴ��� �Լ�
# isdigit() == ���� ���ڰ� '����' ������� �������� ������ True�� ��ȯ�ϴ� �Լ�. 
# isnumeric() == ���ڰ� ǥ���� �ش��ϴ� ���ڿ����� ����

print(solution("aAb1B2cC34oOp"))