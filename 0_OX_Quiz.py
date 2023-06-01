# 덧셈, 뺄셈 수식들이 'X [연산자] Y = Z' 형태로 들어있는 문자열 배열 quiz가 매개변수로 주어집니다.
# 수식이 옳다면 "O"를 틀리다면 "X"를 순서대로 담은 배열을 return하도록 solution 함수를 완성해주세요.

def solution(quiz):
    answer = []
    for n in quiz:
        a,b = n.split("=")
        if eval(a) == int(b):
            answer.append("O")
        else:
            answer.append("X")
    return answer

# def valid(equation):
#     equation = equation.replace('=', '==')
#     return eval(equation)
# def solution(equations):
#     return ["O" if valid(equation) else "X" for equation in equations]    


print(solution(["3 - 4 = -3", "5 + 6 = 11"]))