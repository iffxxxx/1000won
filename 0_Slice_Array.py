# ���� �迭 numbers�� ���� num1, num2�� �Ű������� �־��� ��,
# numbers�� num1�� ° �ε������� num2��° �ε������� �ڸ� ���� �迭�� return �ϵ��� solution �Լ��� �ϼ��غ�����.

def solution(numbers, num1, num2):
    answer = numbers[num1 : num2 + 1]
    return answer

print(solution([1, 2, 3, 4, 5], 1, 3))