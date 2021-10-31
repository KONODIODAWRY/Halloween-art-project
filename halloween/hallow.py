import turtle as trtl
import random
wn = trtl.Screen()
gifs=['ghost.gif', 'skull.gif', 'smile.gif']
#the names are changed in the replit
for i in gifs:
	wn.addshape(i)
t=trtl
n=0
def spin(x,y):
  t.penup()
  t.circle(40)
wn.bgpic("fog.gif")
t.shape(random.choice(gifs))
t.onclick(spin)
wn.mainloop()
