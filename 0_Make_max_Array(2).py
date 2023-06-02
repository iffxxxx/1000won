# 정수 배열 numbers가 매개변수로 주어집니다.
# numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.


def solution(numbers):
    numbers = sorted(numbers)
    return max(numbers[0] * numbers[1], numbers[-1]*numbers[-2]) 

# sort() 메서드는 리스트를 직접 변경하여 정렬하는 파괴적(mutating)인-place 정렬입니다.
# 이는 원래의 리스트를 수정하여 정렬된 순서로 변경합니다.
# 반면에 sorted() 함수는 원래의 리스트를 변경하지 않고 정렬된 새로운 리스트를 반환하는 비파괴적(non-mutating) 정렬입니다.
# 새로운 리스트는 기존 리스트와는 다른 객체로 생성됩니다. 원래의 리스트는 그대로 유지됩니다.
# 파괴적인 sort() 메서드를 사용하면 메모리 사용량이 줄어들고, 정렬된 결과를 원래의 리스트에서 직접 확인할 수 있습니다.
# 비파괴적인 sorted() 함수는 원래의 리스트를 유지하면서 정렬된 새로운 리스트를 얻을 수 있습니다.
# 이는 원래의 리스트를 보존해야 할 때 유용합니다.
# 따라서 선택은 사용하는 상황과 개발자의 선호도에 따라 달라집니다.
# 파괴적인 sort() 메서드는 원래의 리스트를 변경하고자 할 때 사용하고,
# 비파괴적인 sorted() 함수는 원래의 리스트를 보존하면서 정렬된 새로운 리스트를 사용하고자 할 때 사용합니다.

# 테스트 케이스 2번 오류
# def solution(numbers): 
#     num = sorted([i for i in numbers if i != 0])
#     print(num)
#     if len(num) < 2:
#         return 0
#     a = num[0] * num[1]
#     if a >= num[-1] * num[-2]:
#         return a
#     else:
#         return num[-1] * num[-2]
    
print(solution([0,0]))
