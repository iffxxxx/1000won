# 정수 배열 array가 매개변수로 주어질 때, 가장 큰 수와 그 수의 인덱스를 담은 배열을 return 하도록 solution 함수를 완성해보세요.

def solution(array):
    return [n := sorted(array)[-1], array.index(n)]
# := 할당 표현식 n에 값을 넣고 이후에 n을 사용할 수 있음

# def solution(array):
#     return [max(array), array.index(max(array))]
# max함수가 있었다

print(solution([9, 10, 11, 8]))