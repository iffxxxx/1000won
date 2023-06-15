# 선분 3개가 평행하게 놓여 있습니다.
# 세 선분의 시작과 끝 좌표가 [[start, end], [start, end], [start, end]] 형태로 들어있는 2차원 배열 lines가 매개변수로 주어질 때,
# 두 개 이상의 선분이 겹치는 부분의 길이를 return 하도록 solution 함수를 완성해보세요.

def solution(lines):
    lines.sort(key = lambda x : x[0])
    a = lines[0][0]
    print(lines)
    lines.sort(key = lambda x : x[1])
    b = lines [2][1]

    line = []
    for i in range(0, b + 201):
        line.append(0)
    
    for m, n in lines:
        for j in range(m + 100, n + 100):
            line[j] += 1
    answer = line.count(2) + line.count(3)
    return answer


# def solution(lines):
#     sets = [set(range(min(l), max(l))) for l in lines]
#     return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])


print(solution([[0, 5], [1, 10], [3, 9]]))