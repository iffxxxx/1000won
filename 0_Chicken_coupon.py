# ���α׷��ӽ� ġŲ�� ġŲ�� ���Ѹ����� �� ������ ������ �� �� �߱��մϴ�.
# ������ �� �� ������ ġŲ�� �� ���� ���񽺷� ���� �� �ְ�, ���� ġŲ���� ������ �߱޵˴ϴ�.
# ���Ѹ��� ġŲ�� �� chicken�� �Ű������� �־��� �� ���� �� �ִ� �ִ� ���� ġŲ�� ���� return�ϵ��� solution �Լ��� �ϼ����ּ���.

def solution(chicken):
    answer = 0
    while chicken >= 10:
        div = chicken // 10
        mod = chicken % 10
        answer += div
        chicken = div + mod
    return answer


# def solution(chicken):
#     return int(chicken*0.11111111111)

print(solution(1081))

# 199 9 - 19 1 + 8 - 1 1 + 7 - 0 8
# 199   19  1+1   1
# 9     18  17    7