'''
#1번 문제
for i in range(2,10): #[2,3,4,5,6,7,8,9]
    print("{}단".format(i))
    for j in range(1,10): #[1,2,3,4,5,6,7,8,9]
        print("{} x {} = {}".format(i,j,i*j))

#2번 문제
dict_data = {
    "name" : "Ilsun Choi",
    "age" : 99,
    "gender" : "male",
    "account" : 10000,
    "address" : "Republic Of Korea",
    "hobby" : ["swimming", "reading"],
    "famliy" : {"father" : "Choi", "Mather" : "Lim", "brother" : "Choi Sun"},
    "company" : "boanproject"
}

for key in dict_data.keys(): #['name','age','gender' ... ]
    print("{} : {}".format(key, dict_data[key]))
'''
#3번 문제
count = 0
str8 = str(8)

for i in range(1,10000,1): #[1,2,3,4,.. 1188 ...]
    num_str = str(i) # 1188 --> "1188"
    for j in num_str: #[1,1,8,8] index [0,1,2]
        if j==str8:
            count+=1 # count = count + 1
            
print("count : {}".format(count))
