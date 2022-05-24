
# importing libraries
import turtle
import random



t = turtle.Turtle()


w = turtle.Screen()


t.speed(0)
w.bgcolor("black")

t.color("white")

w.title("Mior Azam")

def stars():
	for i in range(5):
		t.fd(10)
		t.right(144)


#STAR LOOP
for i in range(100):
	
	
	x = random.randint(-640, 640)
	y = random.randint(-330, 330)
	
	
	stars()
	
	
	t.up()
	
	
	t.goto(x, y)
	
	
	t.down()

t.up()
t.goto(100, 170)
t.down()
t.color("yellow")

t.begin_fill()

t.circle(40)

t.end_fill()

# write text
# styling font
turtle.color('deep pink')
style = ('Courier', 16, 'italic')
turtle.write('Can we go stargazing together , Mior?', font=style, align='center')
turtle.hideturtle()

t.hideturtle()

w.exitonclick()
