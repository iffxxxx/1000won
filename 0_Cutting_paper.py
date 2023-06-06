# 정수 M, N이 매개변수로 주어질 때,
# M x N 크기의 종이를 최소로 가위질 해야하는 횟수를 return 하도록 solution 함수를 완성해보세요.

def solution(M, N):
    answer = M * N - 1
    return answer


# def get_cut_cnt_dfs(width, height):
#     width, height = min(width, height), max(width, height)
#     if width == 1 and height == 1:
#         return 0
#     return 1 + get_cut_cnt_dfs(width, height//2) + get_cut_cnt_dfs(width, height-height//2)

# def solution(M, N):
#     return get_cut_cnt_dfs(M, N)

# min(width, height)를 사용하여 작은 값을 width, 큰 값을 height로 지정합니다. 이렇게 하면 항상 width가 작은 값이 됩니다.
# 만약 width와 height가 모두 1인 경우, 더 이상 자를 필요가 없으므로 0을 반환합니다.
# 그렇지 않은 경우, 1 + get_cut_cnt_dfs(width, height//2) + get_cut_cnt_dfs(width, height-height//2)를 반환합니다.
# 첫 번째 재귀 호출은 width는 그대로 유지하고 height를 절반으로 자르는 경우의 자르기 횟수를 계산합니다.
# 두 번째 재귀 호출은 width는 그대로 유지하고 height에서 height//2를 뺀 나머지를 자르는 경우의 자르기 횟수를 계산합니다.
# 1을 더해준 이유는 현재 단계에서 자르는 횟수를 더해주기 위해서입니다.

print(solution(2, 5))