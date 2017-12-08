# 가장 기본적인 파일 입출력
f = open('file_name.txt','w')# 파일 열기 = ( 파일 읽겠다, 파일 쓰겠다.)
f.write("가장 기본적인 파일 입출력")
f.close()


f = open('file_name.txt','r')
data = f.read()
print(data)
f.close()

# handle을 다루기 쉬운 방법
with open('file_name_easy.txt','w') as f:
    f.write('handle을 다루기 쉬운 방법')

with open('file_name_easy.txt','r') as f:
    data = f.read()
    print(data)

