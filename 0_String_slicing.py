# ���ڿ� my_str�� n�� �Ű������� �־��� ��, my_str�� ���� n�� �߶� ������ �迭�� return�ϵ��� solution �Լ��� �ϼ����ּ���.

def solution(my_str, n):
    answer = list(map(lambda x: my_str[x : x + n], range(0, len(my_str), n)))
    return answer


# def solution(my_str, n):
#     return [my_str[i: i + n] for i in range(0, len(my_str), n)]
# �����̽��� �ε����� �ʰ��ص� ������ ���� �ʽ��ϴ�.

print(solution("abc1Addfggg4556b", 6))