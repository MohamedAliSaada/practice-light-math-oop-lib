#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import import_ipynb
from .core_math import Number, Vector2D ,Fraction
from .geometry2d import Point, Line 
from math import sqrt ,pi

# -----------------------------------------------
# Base Class for Shapes
# -----------------------------------------------

# -----------------------------------------------
# Base Class for Shapes
# -----------------------------------------------
class Shape:
    """
    Base class for all geometric shapes.
    """
    def area(self):
        raise NotImplementedError("Subclasses must implement the area method.")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement the perimeter method.")

    def SAADA(self):
        return "I inherit this from my father Shape, and you need to polymorphically override me."

# -----------------------------------------------
# Rectangle Class (Inherits from Shape)
# -----------------------------------------------
class Rectangle(Shape):
    """
    Represents a rectangle defined by two corners (bottom-left and top-right).
    """
    def __init__(self, bottom_left, top_right):
        if not isinstance(bottom_left, Point) or not isinstance(top_right, Point):
            raise ValueError("Both bottom_left and top_right must be of type Point.")
        self.bottom_left = bottom_left
        self.top_right = top_right

    def area(self):
        width = abs(self.top_right.getx().get() - self.bottom_left.getx().get())
        height = abs(self.top_right.gety().get() - self.bottom_left.gety().get())
        return width * height

    def perimeter(self):
        width = abs(self.top_right.getx().get() - self.bottom_left.getx().get())
        height = abs(self.top_right.gety().get() - self.bottom_left.gety().get())
        return 2 * (width + height)

# -----------------------------------------------
# Triangle Class (Inherits from Shape)
# -----------------------------------------------
class Triangle(Shape):
    """
    Represents a triangle defined by three vertices.
    """
    def __init__(self, p1, p2, p3):
        if not isinstance(p1, Point) or not isinstance(p2, Point) or not isinstance(p3, Point):
            raise ValueError("All vertices must be of type Point.")
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def area(self):
        x1, y1 = self.p1.getx().get(), self.p1.gety().get()
        x2, y2 = self.p2.getx().get(), self.p2.gety().get()
        x3, y3 = self.p3.getx().get(), self.p3.gety().get()
        return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2

    def perimeter(self):
        side1 = self.p1.distance_to(self.p2)
        side2 = self.p2.distance_to(self.p3)
        side3 = self.p3.distance_to(self.p1)
        return side1 + side2 + side3

# -----------------------------------------------
# Circle Class (Inherits from Shape)
# -----------------------------------------------
class Circle(Shape):
    """
    Represents a circle defined by its center and radius.
    """
    def __init__(self, center, radius_line):
        if not isinstance(center, Point):
            raise ValueError("Center must be of type Point.")
        if not isinstance(radius_line, Line):
            raise ValueError("Radius must be of type Line.")
        if not center.is_equal(radius_line.getp1()):
            raise ValueError("The center must match the starting point of the radius line.")

        self.center = center
        self.radius_line = radius_line

    def area(self):
        radius = self.radius_line.length()
        return pi * (radius ** 2)

    def perimeter(self):
        radius = self.radius_line.length()
        return 2 * pi * radius

    def contains(self, point):
        if not isinstance(point, Point):
            raise ValueError("Point must be of type Point.")
        return self.center.distance_to(point) <= self.radius_line.length()

# -----------------------------------------------
# Polygon Class (Inherits from Shape)
# -----------------------------------------------
class Polygon(Shape):
    """
    Represents a polygon defined by a list of vertices (Points).
    """
    def __init__(self, vertices):
        if not all(isinstance(vertex, Point) for vertex in vertices):
            raise ValueError("All vertices must be of type Point.")
        if len(vertices) < 3:
            raise ValueError("A polygon must have at least 3 vertices.")
        self.vertices = vertices

    def area(self):
        """
        Calculate the area of the polygon using the Shoelace formula.
        """
        n = len(self.vertices)
        area = 0
        for i in range(n):
            x1, y1 = self.vertices[i].getx().get(), self.vertices[i].gety().get()
            x2, y2 = self.vertices[(i + 1) % n].getx().get(), self.vertices[(i + 1) % n].gety().get()
            area += x1 * y2 - y1 * x2
        return abs(area) / 2

    def perimeter(self):
        """
        Calculate the perimeter of the polygon by summing the lengths of its edges.
        """
        n = len(self.vertices)
        perimeter = 0
        for i in range(n):
            perimeter += self.vertices[i].distance_to(self.vertices[(i + 1) % n])
        return perimeter


# In[118]:





# In[ ]:



