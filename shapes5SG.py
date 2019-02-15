from graphics import*

winY = 1000
winX = 1000
#Create Window

window = GraphWin("5 Shapes",1000,1000)
window.setCoords(0,0,1000,1000)

#First Shape: Blue Triangle

triangle = Polygon(Point(0,0),Point(50,100),Point(100,0))
triangle.setFill(color_rgb(255,255,0))
triangle.draw (window)

#Second Shape: Red Square

square = Rectangle(Point(1000,0),Point(900,100))
square.setFill(color_rgb(230,30,30))
square.draw (window)

#Third Shape: Pink Circle
circle = Circle(Point(60,940),60)
circle.setFill(color_rgb(255,123,146))
circle.draw (window)

#Fourth Shape: Orange Oval
oval = Oval(Point(1000,1000),Point(750,850))
oval.setFill(color_rgb(255,136,0))
oval.draw (window)

#Final Shape: Rhombus
diamond = Polygon(Point(400,500),Point(500,600),Point(600,500),Point(500,400))
diamond.setFill(color_rgb(30,30,230))
diamond.draw (window)
