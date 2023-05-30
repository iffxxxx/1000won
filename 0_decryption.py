# 군 전략가 머쓱이는 전쟁 중 적군이 다음과 같은 암호 체계를 사용한다는 것을 알아냈습니다.
# 암호화된 문자열 cipher를 주고받습니다.
# 그 문자열에서 code의 배수 번째 글자만 진짜 암호입니다.
# 문자열 cipher와 정수 code가 매개변수로 주어질 때 해독된 암호 문자열을 return하도록 solution 함수를 완성해주세요.

def solution(cipher, code):
    answer = ""
    for i in range(code - 1, len(cipher), code):
        answer += cipher[i]
    return answer


# def solution(cipher, code):
#     answer = cipher[code-1::code]
#     return answer
# cipher[code-1::code] == cipher 문자열에서 인덱스가 code-1부터 시작하여 code 간격(step)으로 문자를 추출하는 것을 의미

print(solution("pfqallllabwaoclk", 2))