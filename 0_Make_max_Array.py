# ���� �迭 numbers�� �Ű������� �־����ϴ�.
# numbers�� ���� �� �� ���� ���� ���� �� �ִ� �ִ��� return�ϵ��� solution �Լ��� �ϼ����ּ���.

def solution(numbers):
    a = numbers.pop(numbers.index(max(numbers)))
    b = numbers.pop(numbers.index(max(numbers)))
    answer = a * b
    return answer

# pop()�� �� ������ ��Ҹ� ���, pop(n)�� n��° ��� ����


# def solution(numbers):
#     numbers.sort()
#     return numbers[-2] * numbers[-1]

# def solution(numbers):
#     numbers.sort(reverse=True)
#     return numbers[0]*numbers[1]

print(solution([1, 2, 3, 4, 5]))