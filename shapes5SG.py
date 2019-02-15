from graphics import*

#Create Window

window = GraphWin("5 Shapes",1000,1000)
window.setCoords(0,0,1000,1000)

#First Shape: Blue Triangle

triangle = Polygon (Point(0,0),Point(50,100),Point(100,0))
triangle.setFill(color_rgb(30,30,230))
triangle.draw (window)
