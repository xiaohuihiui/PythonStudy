from gamegrid import *
from random import randint
#fish=Actor("sprites/babelfish.gif")
#
#
#repeat:
#    fish.move(1)
#    field.refresh()
#    delay(20)
#    if fish.getX()>630:
#     fish.setX(-30)

class Fish(Actor):
    speed=1
    def act(self):
      self.move(self.speed)
      if self.getX()>630:
       self.setX(-30)
field=GameGrid(600,600,1,None,"sprites/reef.gif",True)
field.setTitle('game') 
x = 50
y = 50
repeat 10:    
  fish=Fish("sprites/babelfish.gif")
  fish.speed=randint(1,20)
  field.addActor(fish,Location(x,y))
  x += 50
  y += 50
field.setSimulationPeriod(20)
field.show()
field.doRun()
