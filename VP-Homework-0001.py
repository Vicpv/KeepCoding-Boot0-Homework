import turtle as tu

tu.shape("turtle")

tu.back(350)
tu.pencolor("red")
for i in range(4):
    tu.forward(100)
    tu.left(90)

tu.forward(260)
tu.left(90)
tu.forward(100)
tu.left(90)
tu.forward(260)

tu.pencolor("blue")
for i in range(3):
    tu.right(120)
    tu.forward(100)

tu.back(260)
tu.right(60)
tu.forward(100)
tu.left(60)
tu.forward(160)
tu.left(60)
tu.forward(100)
tu.left(30)
tu.pencolor("red")
tu.forward(100)
tu.right(90)
tu.forward(100)

tu.back(40)
tu.right(90)
tu.pencolor("black")
tu.forward(50)
tu.right(90)

tu.begin_fill()

tu.pencolor("green")
for i in range(8):
    tu.forward(20)
    tu.left(45)
tu.end_fill()

tu.pencolor("black")
tu.forward(20)
tu.right(90)
tu.forward(50)
tu.right(90)

tu.back(70)

tu.pencolor("yellow")
tu.right(90)
tu.forward(50)
tu.right(90)
tu.forward(25)
tu.right(90)
tu.forward(50)

tu.pencolor("black")
tu.right(90)
tu.forward(50)
tu.pencolor("brown")
tu.forward(100)
tu.back(450)

tu.forward(150)

tu.right(90)
tu.forward(25)
tu.left(90)
tu.forward(80)
tu.left(90)
tu.forward(25)
tu.left(90)
tu.forward(80)