#오른쪽 표를 토대로 dict b를 만들고 다음을 구현하라.
b = {'name' : 'John',
     'phone' : '01012345432',
     'email' : 'test@test.com',
     'birth' : 111111
     }
print('b: ', b)
#dict b에서 name 데이터를 찾으라.
print("b['name']:", b['name'])
#dict b에서 birth 데이터를 101010으로 바꿔라.
b['birth'] = 101010
print("b['birth']:", b['birth'])
#dict b에 key가 city이고 value가 Seoul인 데이터를 추가하라.
b['city'] = 'Seoul'
print("b['city']:", b['city'])
