'''
사용한 함수
forward(앞으로 가기)
right(오른쪽으로회전)
left(왼쪽으로 회전)
penup(펜 올리기)
pendown(펜 내리기)
goto(지정한 좌표로 이동)
fillcolor(색채우기)
circle(원그리기)
speed(그림그리는 속도)
color(펜색상 변경)
'''
import turtle
t=turtle.Turtle()
t.speed(10)
#산을 그린다.
t.penup()
t.goto(-300,100) #왼쪽 끝으로 좌표이동
t.pendown()
t.right(60)
col=['olivedrab','darkolivegreen','olive'] #색상을 리스트에 넣어둔다
for i in range(3):
    t.fillcolor(col[i])#반복문을 이용해 3가지 색을 각각 채워준다.
    t.begin_fill()
    t.left(120)
    t.fd(200)
    t.right(120)
    t.fd(200)
    t.end_fill()
t.penup()

#집을 그린다
t.color('pink')
t.goto(-120,-40)#좌표이동
t.pendown()
t.right(120)#지붕그리기
t.fd(150)
t.right(120)
t.fd(50)
t.right(60)
t.fd(100)
t.right(60)
t.fd(50)
t.right(120)

t.fd(10)#집 몸통 그리기
t.left(90)
t.fd(120)
t.right(90)
t.fd(130)
t.right(90)
t.fd(120)

t.penup()
t.right(135)#창문그리기
t.fd(20)
t.left(45)
t.pendown()
t.fd(40)
t.right(90)
t.fd(40)
t.right(90)
t.fd(40)
t.right(90)
t.fd(40)

#빨간나무 그리기
t.color('black')
t.penup()
t.goto(80,-100)
t.pendown()
t.right(90)
t.fillcolor('red') #빨간 잎부분 
t.begin_fill()
t.penup()
t.circle(60,20) #나무가지가 있을 부분을(40도) 비우고 그리기 위해서 펜을 들고 이동후
t.pendown()
t.circle(60,320) #남은 부분을 그려준다
t.penup()
t.circle(60,40)
t.end_fill()
t.pendown()
t.fillcolor('saddlebrown')#나무부분
t.begin_fill()
t.left(40)#가지부분
t.fd(60)
t.left(165)
t.fd(60)
t.right(130)
t.fd(80)
t.left(170)
t.fd(80)
t.right(130)
t.fd(60)
t.left(165)
t.fd(60)
t.right(30)#나무 몸통부분
t.fd(100)
t.left(90)
t.fd(40)
t.left(90)
t.fd(100)
t.end_fill()

#노란나무그리기(빨간나무와 같은방법으로 그린다)
t.penup()
t.goto(200,-100)
t.pendown()
t.right(90)
t.fillcolor('yellow')
t.begin_fill()
t.penup()
t.circle(60,20)
t.pendown()
t.circle(60,320)
t.penup()
t.circle(60,40)
t.end_fill()
t.pendown()
t.fillcolor('saddlebrown')
t.begin_fill()
t.left(40)
t.fd(60)
t.left(165)
t.fd(60)
t.right(130)
t.fd(80)
t.left(170)
t.fd(80)
t.right(130)
t.fd(60)
t.left(165)
t.fd(60)
t.right(30)
t.fd(100)
t.left(90)
t.fd(40)
t.left(90)
t.fd(100)
t.end_fill()

#화면 클릭할때마다 랜덤하게 날리는 나뭇잎 나타나게 하기
import turtle
from random import *
t=turtle.Turtle()
s=turtle.Screen()

#단풍잎그리는 함수
def Maple(n):
    t.speed(10)
    t.left(90)
    for i in range(6):
        t.fillcolor('red')
        t.begin_fill()
        t.fd(n)
        t.left(160)
        t.fd(n*2/3)
        t.right(80)
        t.fd(n*2/3)
        t.left(160)
        t.fd(n)
        t.end_fill()
        t.right(180)

#은행잎그리는 함수       
def Ginkgo(n):
    t.speed(10)
    t.left(120)
    t.fillcolor('yellow')
    t.begin_fill()
    t.circle(n,120)
    t.left(90)
    t.forward(n)
    t.left(60)
    t.fd(n)
    t.end_fill()
    t.right(180)
    t.fd(n)
    t.left(60)
    t.fd(n*1/2)

#일반갈색나뭇잎그리는 함수    
def Leaf(n):
    t.speed(10)
    t.fillcolor('brown')
    t.begin_fill()
    t.left(45)
    t.circle(n,90)
    t.left(90)
    t.circle(n,90)
    t.end_fill()
    t.left(135)
    t.fd(n*1.8)
    

def drawit(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    k=randint(1,3)
    if k==1:
        n=randint(10,30)
        Maple(n)
    elif k==2:
        n=randint(10,30)
        Ginkgo(n)
    elif k==3:
        n=randint(10,30)
        Leaf(n)

s.onscreenclick(drawit)









    


    
