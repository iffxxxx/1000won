# ������ ��� �ִ� �迭 num_list�� �Ű������� �־����ϴ�.
# num_list�� ������ ������ �Ųٷ� ������ �迭�� return�ϵ��� solution �Լ��� �ϼ����ּ���.

def solution(num_list):
    answer = []
    for i in range(len(num_list)-1, -1, -1):
        answer.append(num_list[i])
    return answer


# def solution(num_list):
#     answer = []
#     for i in range(1,len(num_list)+1):
#         answer.append(num_list[-i])
#     return answer


# def solution(num_list):
#     return num_list[::-1]


# def solution(num_list):
#     num_list.reverse()
#     return num_list


# def solution(num_list):
#     result =[]
#     while(num_list):
#         result.append(num_list.pop())
#     return result

print(solution([1, 2, 3, 4, 5]))