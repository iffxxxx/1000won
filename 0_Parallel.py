# 점 네 개의 좌표를 담은 이차원 배열  dots가 다음과 같이 매개변수로 주어집니다.
# [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
# 주어진 네 개의 점을 두 개씩 이었을 때, 두 직선이 평행이 되는 경우가 있으면 1을 없으면 0을 return 하도록 solution 함수를 완성해보세요.

def gradiant(dotA, dotB):
    dx = dotB[0] - dotA[0]
    dy = dotB[1] - dotA[1]
    return dy / dx

def solution(dots):
    dots.sort(key = lambda x:x[0])
    a, b, c, d = dots

    d1 = gradiant(a, b)
    d2 = gradiant(c, d)

    if d1 == d2:
        return 1
    return 0

# 실패한 케이스 - 테스트케이스 1, 10
# def solution(dots):
#     dots.sort()
#     print(dots)
#     if dots[2][0] - dots[0][0] == dots[3][0] - dots[1][0]:
#         if dots[2][1] - dots[0][1] == dots[3][1] - dots[1][1]:
#             return 1
#     return 0

print(solution([(0,0),(1,0),(3,3),(4,3)]))