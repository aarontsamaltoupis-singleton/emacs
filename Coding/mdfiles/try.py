class Point: 
    def move(self):
        return 3


point1 = Point()
point1.move()

point1.x = 3
point1.y  = 3

print(point1.x, point1.y, point1.move())
