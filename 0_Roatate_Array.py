# ������ ��� �迭 numbers�� ���ڿ� direction�� �Ű������� �־����ϴ�.
# �迭 numbers�� ���Ҹ� direction�������� �� ĭ�� ȸ����Ų �迭�� return�ϵ��� solution �Լ��� �ϼ����ּ���.

def solution(numbers, direction):
    answer = []
    if direction == "right":
        answer = [numbers[-1]] + numbers[0:-1]
    elif direction == "left":
        answer = numbers[1:] + [numbers[0]]
    return answer

print(solution([1,2,3], "right"))