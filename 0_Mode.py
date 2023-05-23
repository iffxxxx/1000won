# 최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 
# 정수 배열 array가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요. 최빈값이 여러 개면 -1을 return 합니다.

def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            # print(set(array))
            # print(i, a)
            array.remove(a)
        if i == 0:
            return a
    return -1

print(solution([1, 1, 1, 2, 2, 3]))