# 머쓱이는 친구들과 369게임을 하고 있습니다.
# 369게임은 1부터 숫자를 하나씩 대며 3, 6, 9가 들어가는 숫자는 숫자 대신 3, 6, 9의 개수만큼 박수를 치는 게임입니다.
# 머쓱이가 말해야하는 숫자 order가 매개변수로 주어질 때, 머쓱이가 쳐야할 박수 횟수를 return 하도록 solution 함수를 완성해보세요.

def solution(order):
    answer = [i for i in str(order) if (i in '369')]
    return len(answer)


# def solution(order):
#     return sum(map(lambda x: str(order).count(str(x)), [3, 6, 9]))
# map() 함수는 리스트 [3, 6, 9] 각 요소에 lambda 함수를 적용함


print(solution(29423))