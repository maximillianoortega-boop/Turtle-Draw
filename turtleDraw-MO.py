import turtle

TEXTFILENAME = 'Turtle-Draw.txt'

print ('TD-lite - pt 3')

TDscreen = turtle.screen()
TDscreen.setup(450, 450)

TD = turtle.Turtle()
TD.speed(0)
TD.penup()

print ('TD Lite running it up!!!')
turtleDrawTextFile = open(TEXTFILENAME, 'r')
line = turtleDrawTextFile.readline()
while line:
    print(line, end='')
    parts = line.split(' ')

    if (len(parts) == 3):
        color = parts[0]
        x = int(parts[1])
        y = int(parts[2])

        TD.color(color)
        TD.goto(x,y)
        TD.pendown()
        
    if(len(parts) == 1):
        TD.penup()

    line = turtleDrawTextFile.readline()


turtle.done()
turtleDrawTextFile.close()
print ("\nEnd")



