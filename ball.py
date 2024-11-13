import turtle

class ball:

    def __init__(self, color="", size=0, x=0, y=0, speed = (0,0)):
        self.color = color
        self.__size = size
        self.x = x
        self.y = y
        self.__speed = speed

    def draw_ball(self):
        turtle.penup()
        turtle.color(self.color)
        turtle.fillcolor(self.color)
        turtle.goto(self.x, self.y - self.size)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.size)
        turtle.end_fill()

    def move_ball(self, dt):
        self.x += self.speed[0] * dt
        self.y += self.speed[1] * dt

    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        self.__size = value

    @property
    def speed(self):
        return self.__speed
    @speed.setter
    def speed(self, value):
        self.__speed = value





