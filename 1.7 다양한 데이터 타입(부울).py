#변수 x에 숫자 하나를 사용자로부터 입력 받는다.
x = float(input('x? '))
#x가 10보다 큰 지 검사하여 Boolean 값을 출력하라.
print(bool(x > 10))
#x의 데이터 형이 float인지 검사하여 Boolean 값을 출력하라.
print(str(type(x)) == "<class 'float'>")
#x가 0인지 검사하여 Boolean 값을 출력하라.
print(x == 0)
#x가 0이 아닌지 검사하여 Boolean 값을 출력하라.(not)
print(not (x == 0))
#x가 0이거나 10보다 큰 지 검사하여 Boolean 값을 출력하라.(and, or)
print((x == 0) or (x > 10))
