# 정수 n이 매개변수로 주어질 때 n의 각 자리 숫자의 합을 return하도록 solution 함수를 완성해주세요

def solution(n):
    return sum([int(i) for i in str(n)])


# def solution(n):
#     answer = 0
#     while n:
#         n, r = divmod(n, 10)
#         answer += r
#     return answer
# divmod() == 두 개의 숫자를 인자로 받아, 첫번 째 숫자를 두번 째 숫자로 나눈 몫과 나머지를 튜플(tuple) 형태로 반환

print(solution(1234))