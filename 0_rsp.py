# 가위는 2 바위는 0 보는 5로 표현합니다.
# 가위 바위 보를 내는 순서대로 나타낸 문자열 rsp가 매개변수로 주어질 때, rsp에 저장된 가위 바위 보를 모두 이기는 경우를 순서대로 나타낸 문자열을 return하도록 solution 함수를 완성해보세요.

def solution(rsp):
    answer = ''
    rsp_win = {'2':'0', '0':'5', '5':'2'}
    for i in rsp:
        answer += rsp_win[i]
    return answer
    # return ''.join(rsp_win[i] for i in rsp)


# def solution(rsp):
#     return rsp.translate(str.maketrans('025', '502'))
# str.maketrans = 첫번재 인수와 두번째 인수의 각 문자를 지정
# translate = 각 문자를 대응되는 문자로 치환하는 기능

print(solution("205"))