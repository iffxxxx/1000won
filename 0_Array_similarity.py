# 두 배열이 얼마나 유사한지 확인해보려고 합니다.
# 문자열 배열 s1과 s2가 주어질 때 같은 원소의 개수를 return하도록 solution 함수를 완성해주세요.

def solution(s1, s2):
    answer = 0
    for i in s1:
        if i in s2:
            answer += 1
    return answer

# def solution(s1, s2):
#     return len(set(s1)&set(s2))
# s1&s2 != unsupported operand type(s) for &: 'list' and 'list'
# & 는 교집합 - 리스트 타입은 집합 연산을 지원하지 않음 - 집합으로 변환이 필요하다

print(solution(["a", "b", "c"], ["com", "b", "d", "p", "c"]))