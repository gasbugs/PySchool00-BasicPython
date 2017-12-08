#1. 오른쪽 그림과 같은 집합을 생성하고 다음 물음에 답하라.
#집합 A, B, C를 각각 선언하라.
A = {'a','a','b','b','c','a','h','d','h','e','f','g','g'}
B = {'h','d','h','e','f','o','k','l','l','k','i','m','m'}
C = {'g','g','e','f','i','j','j','n','n','p','p'}
print('A', A)
print('B', B)
print('C', C)
#집합 A와 B의 합집합을 구하라.
print("A와 B의 합집합", A|B)
#집합 A와 C의 차집합을 구하라.
print("A와 C의 차집합", A-C)
#집합 A와 B, C의 교집합을 구하라.
print("A, B, C의 교집합", A&B&C)

#2. 과일에 대한 데이터를 다음과 같이 입력했을 때 중복된 값이 제외된 상태로 출력되도록 변수를 선언하고 출력하십시오.
#입력 : melon banana strawberry melon banana blueberry banana strawberry
#출력 : {'strawberry', 'blueberry', 'melon', 'banana'}

x = input('입력 : ') #melon banana strawberry melon banana blueberry banana strawberry
x = x.split()
print(set(x))
