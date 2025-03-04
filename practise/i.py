##none=True
##while none:
##    number=int(input('input numaber'))
##    if number==1:
##        print("13")
##    elif number==2:
##        print('42')
##    else:
##        continue
##    
##
##import turtle
##
##t=turtle.Pen()
##colors=['red','blue','yellow','green']
##for x in range(100):
##    t.pencolor(colors[x%4])
##    t.circle(x)
##    t.right(90)

##import turtle
##t=turtle.Pen()
##colors=['red','green','yellow','blue','orange']
##for x in range(100):
## t.pencolor(colors[x%5])
## t.circle(x)
## t.right(90)

##number=['1','2','1','2','1','2','1','2','1','2','1','2','1','2','1','2']
##numberOne=[]
##numberTwo=[]
##
##for i in number:
##    if i=='1':
##       numberOne.append(i)
##    elif  i=='2':
##       numberTwo.append(i)
##print(numberOne)
##print(numberTwo)

##rank=('a','b','c','d','e','f','g')
##while True:
##    names=input('name')
##    r=rank.index(names)
##    print(r+1)
##rank={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7}
##while True:
##    names=input('name')
##    r=rank[names]
##    print(r)
##rank={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7}
##
##for a,b in rank.items():
##    print(a, 'value:'+ str(b))
##函数
import turtle
t=turtle.Pen()
colors=['red','blue','yellow','green']
def draw(a,b):
 t.goto(a,b)
 for x in range(20):
  t.pencolor(colors[x%4])
  t.circle(x)
  t.right(90)

draw(100,100)
draw(50,50)
  

















