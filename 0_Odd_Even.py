# ������ ��� ����Ʈ num_list�� �־��� ��,
# num_list�� ���� �� ¦���� Ȧ���� ������ ���� �迭�� return �ϵ��� solution �Լ��� �ϼ��غ�����.

def solution(num_list):
    odd = 0
    even = 0
    for i in num_list:
        if i % 2 == 1:
            odd += 1
        else:
            even += 1
    answer = [even, odd]
    return answer


# def solution(num_list):
#     answer = [0,0]
#     for n in num_list:
#         answer[n%2]+=1
#     return answer


print(solution([1, 2, 3, 4, 5]))