#!/usr/bin/env python
# coding: utf-8

# In[118]:


from math import sqrt, pi
import import_ipynb
from .core_math import Number, Vector2D ,Fraction

# -----------------------------------------------
# Point class: represents a location in 2D space using two Number coordinates
# -----------------------------------------------
class Point:
    def __init__(self, x, y):
        if not isinstance(x, Number) or not isinstance(y, Number):
            raise ValueError("Both inputs must be of type Number")
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def setx(self, xx):
        if not isinstance(xx, Number):
            raise ValueError("Input for x must be of type Number")
        self.__x = xx

    def sety(self, yy):
        if not isinstance(yy, Number):
            raise ValueError("Input for y must be of type Number")
        self.__y = yy

    def __str__(self):
        return f"( {self.__x.get()} , {self.__y.get()} )"

    def distance_to(self, P2):
        if not isinstance(P2, Point):
            raise ValueError("Input must be of type Point")
        dx = P2.getx().get() - self.__x.get()
        dy = P2.gety().get() - self.__y.get()
        return sqrt(dx**2 + dy**2)

    def to_vector(self):
        return Vector2D(self.__x, self.__y)

    def translate(self, vector):
        if not isinstance(vector, Vector2D):
            raise ValueError("Input must be of type Vector2D")
        new_x = Number(self.__x.get() + vector.getx().get())
        new_y = Number(self.__y.get() + vector.gety().get())
        return Point(new_x, new_y)

    def midpoint(self, P2):
        if not isinstance(P2, Point):
            raise ValueError("Input must be of type Point")
        mid_x = Number((self.__x.get() + P2.getx().get()) / 2)
        mid_y = Number((self.__y.get() + P2.gety().get()) / 2)
        return Point(mid_x, mid_y)

    def reflect(self):
        return Point(Number(-self.__x.get()), Number(-self.__y.get()))

    def is_equal(self, P2):
        if not isinstance(P2, Point):
            raise ValueError("Input must be of type Point")
        return self.__x.get() == P2.getx().get() and self.__y.get() == P2.gety().get()

    def slope_with(self, P2):
        if not isinstance(P2, Point):
            raise ValueError("Input must be of type Point")
        dx = P2.getx().get() - self.__x.get()
        dy = P2.gety().get() - self.__y.get()
        if dx == 0:
            raise ZeroDivisionError("Slope is undefined for vertical lines (x1 == x2)")
        return dy / dx

    @classmethod
    def origin(cls):
        return cls(Number(0), Number(0))



# -----------------------------------------------
# Line class: represents a line segment in 2D space using two Point objects
# -----------------------------------------------
class Line:
    def __init__(self, P1, P2):
        if not isinstance(P1, Point) or not isinstance(P2, Point):
            raise ValueError("Both inputs must be of type Point")
        self.__P1 = P1
        self.__P2 = P2

    def getp1(self):
        return self.__P1

    def getp2(self):
        return self.__P2

    def __str__(self):
        return f"{self.__P1} | {self.__P2}"

    def midpoint(self):
        return self.__P1.midpoint(self.__P2)

    def length(self):
        return self.__P1.distance_to(self.__P2)

    def slope(self):
        return self.__P1.slope_with(self.__P2)

    def is_vertical(self):
        return self.__P1.getx().get() == self.__P2.getx().get()

    def is_horizontal(self):
        return self.__P1.gety().get() == self.__P2.gety().get()


        


# In[ ]:





# In[ ]:





# In[ ]:



