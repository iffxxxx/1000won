# 머쓱이는 구슬을 친구들에게 나누어주려고 합니다. 구슬은 모두 다르게 생겼습니다.
# 머쓱이가 갖고 있는 구슬의 개수 balls와 친구들에게 나누어 줄 구슬 개수 share이 매개변수로 주어질 때,
# balls개의 구슬 중 share개의 구슬을 고르는 가능한 모든 경우의 수를 return 하는 solution 함수를 완성해주세요.

def pac(number):
    j = 1
    for i in range(1, number + 1):
        j *= i
    return j

def solution(balls, share):
    answer = pac(balls) / (pac(balls - share) * pac(share))
    return int(answer)


# import math

# def solution(balls, share):
#     return math.comb(balls, share)

print(solution(3, 2))