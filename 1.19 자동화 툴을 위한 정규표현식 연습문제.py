import re

data="""
010-4321-1234
011-4321-1234
032-4321-1234
911111-1234567
999999-1234567
978-89-6848-841-2
978-89-6848-841-4
"""

#1 유효한 핸드폰 전화번호 확인하기
pat = re.compile("01[0-9]-\d{4}[-]\d{4}")
result = pat.findall(data)
print(result)

#2 유효한 주민등록번호 확인하기
pat = re.compile("\d{2}[0-1][0-9][0-3][0-9][-]\d{7}")
result = pat.findall(data)
print(result)

#3 유효한 ISBN 확인하기
pat = re.compile("\d{3}-\d{2}-\d{4}-\d{3}-\d{1}")
result = pat.findall(data)
new_result = []
for i in result:
    i_array=i.replace("-","")
    check_num = 0
    for j in range(len(i_array)-1):
         j_num = int(i_array[j])
         if j % 2 == 0:
             check_num += j_num*1
         else :
             check_num += j_num*3
    x = (10 - (check_num % 10)) %10
    
    if str(x)==i[-1]:
        new_result.append(i)
print(new_result)

