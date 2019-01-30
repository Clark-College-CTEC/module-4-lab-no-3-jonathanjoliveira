# Lab No. 3
# CTEC 121
# Jonathan Oliveira

import graphics

def snowman():
    # create the graphics window
    win = graphics.GraphWin('Lab 3 - Snowman',800,800)
    
    # your code to draw the snowman goes here
    # draw three circles for the body
    # name the three circles circle1, circle2 and circl3

    circle1 = graphics.Circle(graphics.Point(400,600),150)
    circle1.draw(win)
    circle2 = graphics.Circle(graphics.Point(400,350),100)
    circle2.draw(win)
    circle3 = graphics.Circle(graphics.Point(400,175),75)
    circle3.draw(win)


    # draw two eyes on the top circle
    # name the two eyes using variables eye1 and eye2

    eye1 = graphics.Circle(graphics.Point(370,170),25)
    eye1.draw(win)
    eye2 = eye1.clone()
    eye2.move(62.5,0)
    eye2.draw(win)


    # draw a nose using the polygon method and make it orange
    # name the nose using the variable nose

    nose = graphics.Polygon(graphics.Point(401,195),graphics.Point(381,215),graphics.Point(421,215))
    nose.setFill("orange")
    nose.draw(win)


    # draw a hat using a rectangle and fill it with black
    # name the hat using the variable hat

    hat = graphics.Rectangle(graphics.Point(360,69),graphics.Point(440, 95))
    hat.setFill("black")
    hat.draw(win)


    # draw a line to represent the rim of the hat using a line
    # name the line using the variable hatline

    hatLine = graphics.Line(graphics.Point(300,98),graphics.Point(500,98))
    hatLine.setWidth(5)
    hatLine.draw(win)

    arm1 = graphics.Line(graphics.Point(500, 350),graphics.Point(624, 437))
    arm1.draw(win)
    arm2 = graphics.Line(graphics.Point(300,350),graphics.Point(176,437))
    arm2.draw(win)
    

    # close the program
    input('Press enter to quit the program ')
    # close the graphics window
    win.close()


# Call the snowman() function to start the program
snowman()