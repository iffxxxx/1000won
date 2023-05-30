# 정수 배열 array와 정수 n이 매개변수로 주어질 때, array에 들어있는 정수 중 n과 가장 가까운 수를 return 하도록 solution 함수를 완성해주세요.

def solution(array, n):
    Minus = sorted([abs(i - n) for i in array])
    if n - Minus[0] in array:
        answer = n - Minus[0]
    else:
        answer = Minus[0] + n
    return answer


def solution(array, n):
    array.sort(key = lambda x : (abs(x-n), x-n))
    answer = array[0]
    return answer
# lambda == 한 줄로 표현하는 익명 함수
# array.sort(key=lambda x: (abs(x-n), x-n)) == array를 (abs(x-n), x-n) 값으로 정렬하는 것
# sort(key = lambda x : (x[0], x[1]))

# solution=lambda a,n:sorted(a,key=lambda x:(abs(x-n),x))[0]


print(solution([3, 10, 28], 20))