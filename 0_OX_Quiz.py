# ����, ���� ���ĵ��� 'X [������] Y = Z' ���·� ����ִ� ���ڿ� �迭 quiz�� �Ű������� �־����ϴ�.
# ������ �Ǵٸ� "O"�� Ʋ���ٸ� "X"�� ������� ���� �迭�� return�ϵ��� solution �Լ��� �ϼ����ּ���.

def solution(quiz):
    answer = []
    for n in quiz:
        for i, v in enumerate(n.split(" = ")):
            if eval(v) == (int(n.split(" = ")[i + 1])):
                answer.append("O")
                break
            else:
                answer.append("X")
                break
    return answer


# def valid(equation):
#     equation = equation.replace('=', '==')
#     return eval(equation)

# def solution(equations):
#     return ["O" if valid(equation) else "X" for equation in equations]    


print(solution(["3 - 4 = -3", "5 + 6 = 11"]))