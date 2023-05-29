# 숫자와 "Z"가 공백으로 구분되어 담긴 문자열이 주어집니다.
# 문자열에 있는 숫자를 차례대로 더하려고 합니다. 이 때 "Z"가 나오면 바로 전에 더했던 숫자를 뺀다는 뜻입니다.
# 숫자와 "Z"로 이루어진 문자열 s가 주어질 때, 머쓱이가 구한 값을 return 하도록 solution 함수를 완성해보세요.

def solution(s):
    s = s.split()
    for i, j in enumerate(s):
        if j == 'Z':
            s.pop(i - 1)
    answer = sum([int(i) for i in s if (i.lstrip("-").isdigit())])
    return answer
# isdigit 는 음수에서 False를 낸다


# def solution(s):
#     answer = 0
#     for i in range(len(s := s.split(" "))):
#         answer += int(s[i]) if s[i] != "Z" else -int(s[i-1])
#     return answer
# :=는 할당 표현식(assignment expression) 또는 walrus 연산자라고도 불리는 표현식입니다.
# 이 연산자는 변수에 값을 할당하고, 동시에 할당한 값을 반환


# def solution(s):
#     stack = []
#     for a in s.split():
#         if a != 'Z':
#             stack.append(int(a))
#         else:
#             if stack:
#                 stack.pop()
#     return sum(stack)
# if stack: == 'stack'이 비어있지 않은 경우 코드 블록 실행
# stack은 LIFO(Last in First come) 구조 ex. 아이스크림콘, 프링글스통


print(solution("-1 -2 -3 Z"))