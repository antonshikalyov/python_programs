import turtle
turtle.home()
turtle.down()
for move in [30]*12:
    turtle.forward(move)
    turtle.left(move)
    turtle.forward(move)
turtle.color("#a32638")
turtle.right(90)
turtle.up()
turtle.forward(50)
turtle.left(90)
turtle.down()
for move in [40]*12:
    turtle.forward(move)
    turtle.left(move-10)
    turtle.forward(move)
turtle.up()
turtle.forward(-100)
turtle.right(90)
turtle.forward(60)
turtle.left(90)
turtle.down()
turtle.colormode(255)
turtle.color((0,0,0))
turtle.forward(200)
# first line ready
turtle.up()
turtle.right(90)
turtle.forward(60)
turtle.left(90)
turtle.forward(-200)
turtle.down()
turtle.color((100,1,1))
turtle.forward(200)
#second line ready
turtle.up()
turtle.right(90)
turtle.forward(60)
turtle.left(90)
turtle.forward(-200)
turtle.down()
turtle.color((200,2,2))
turtle.forward(200)
#third
input()
