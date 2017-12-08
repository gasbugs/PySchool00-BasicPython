import turtle as t
'''
#세모 그리기
for i in range(3):
    t.fd(100)
    t.left(120)

t.up()
t.fd(200)
t.down()

#오각형 그리기
for i in range(5):
    t.fd(100)
    t.left(360/5)

t.up()
t.fd(200)
t.down()

#별 그리기
for i in range(5):
    t.fd(100)
    t.left(360*2/5)


t.up()
t.fd(200)
t.down()
'''

t.speed(10)
# 이상한 도형 그리기
for i in range(100):
    t.fd(100)
    t.left(360*2/120)
    for j in range(10):
        t.fd(50)
        t.left(360*2/40)

