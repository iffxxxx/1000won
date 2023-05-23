# 정수가 들어 있는 배열 num_list가 매개변수로 주어집니다.
# num_list의 원소의 순서를 거꾸로 뒤집은 배열을 return하도록 solution 함수를 완성해주세요.

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