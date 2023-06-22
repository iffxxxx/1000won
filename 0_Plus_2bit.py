# 이진수를 의미하는 두 개의 문자열 bin1과 bin2가 매개변수로 주어질 때, 두 이진수의 합을 return하도록 solution 함수를 완성해주세요.

def solution(bin1, bin2):
    bin3 = bin(int(bin1, 2) + int(bin2, 2))
    return bin3[2:]

print(solution("1001", 	"1111"))