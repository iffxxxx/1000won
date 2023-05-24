# 정수가 담긴 리스트 num_list가 주어질 때,
# num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 return 하도록 solution 함수를 완성해보세요.

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