import turtle as trtl
import random
wn = trtl.Screen()
gifs=['ghost.gif', 'skull.gif', 'smile.gif']
for i in gifs:
	wn.addshape(i)
t=trtl.Turtle()
u=trtl.Turtle()
u.penup()
u.goto(-250,250)
n=0
s=1
font_setup=("Arial", 20, "normal")
def score():
  global s
  u.clear()
  u.write(s, font=font_setup)
  s+=1
def spin(x,y):
  t.penup()
  t.circle(40)
wn.bgpic("fog.gif")
t.shape(random.choice(gifs))
t.onclick(spin)
u.onclick(score())
wn.mainloop()
