import turtle

with open('kilpkonn.txt', 'r') as f:
    commands = f.read().splitlines()

t = turtle.Turtle()
t.penup()
t.goto(0, 0)
t.pendown()

for command in commands:
    parts = command.split()
    if parts[0] == 'edasi':
        t.forward(int(parts[1]))
    elif parts[0] == 'tagasi':
        t.backward(int(parts[1]))
    elif parts[0] == 'vasakule':
        t.left(int(parts[1]))
    elif parts[0] == 'paremale':
        t.right(int(parts[1]))

num_shapes = int(input("Mitu kujundit soovid joonistada? "))

for i in range(num_shapes):
    t.penup()
    t.goto(i*50, i*50)
    t.pendown()
    for j in range(4):
        t.forward(100)
        t.left(90)

turtle.done()
