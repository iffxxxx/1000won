# �Ӿ��̳� �ʰ��Դ� 10�� �� �̻� ��� 5%, 30�� �� �̻� ��� 10%, 50�� �� �̻� ��� 20%�� �������ݴϴ�.
# ������ ���� ���� price�� �־��� ��, �����ؾ� �� �ݾ��� return �ϵ��� solution �Լ��� �ϼ��غ�����.

def solution(price):
    if price >= 500000:
        answer = price * 0.8
    elif price >= 300000:
        answer = price * 0.9
    elif price >= 100000:
        answer = price * 0.95
    else:
        answer = price
    return int(answer)

# def solution(price):
#     discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
#     for discount_price, discount_rate in discount_rates.items():
#         if price >= discount_price:
#             return int(price * discount_rate)

print(solution(580000))