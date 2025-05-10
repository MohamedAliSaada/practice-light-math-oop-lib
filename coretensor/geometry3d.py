#!/usr/bin/env python
# coding: utf-8

# In[366]:


import import_ipynb
from .core_math import Number, Vector2D ,Fraction
from .geometry2d import Point, Line 
from .advancedgeometry2d import Rectangle,Triangle ,Circle ,Polygon



class Vector3D:
    def __init__(self, x1, x2, x3):
        if not isinstance(x1, Number) or not isinstance(x2, Number) or not isinstance(x3, Number):
            raise ValueError("the input's must be Number Data Type.")
        self.__x1 = x1
        self.__x2 = x2
        self.__x3 = x3

    def getV(self):
        return f"({self.__x1} , {self.__x2} , {self.__x3})"

    # Overloading dunder functions
    def __str__(self):
        return f"({self.__x1} , {self.__x2} , {self.__x3})"

    def __getitem__(self, i):
        if i == 0:
            return self.__x1.get()
        elif i == 1:
            return self.__x2.get()
        elif i == 2:
            return self.__x3.get()
        else:
            raise IndexError("out of index")

    def __setitem__(self, i, value):
        if not isinstance(value, (int, float, Number)):
            raise ValueError("Value must be a number (int, float, or Number).")
        if isinstance(value, (int, float)):
            value = Number(value)

        if i == 0:
            self.__x1 = value
        elif i == 1:
            self.__x2 = value
        elif i == 2:
            self.__x3 = value
        else:
            raise IndexError("out of index")

    def __add__(self, other):
        if not isinstance(other, Vector3D):
            raise ValueError("the input's must be Vector3D Data Type.")
        return Vector3D(
            Number(self.__x1.get() + other[0]),
            Number(self.__x2.get() + other[1]),
            Number(self.__x3.get() + other[2])
        )

    def __sub__(self, other):
        if not isinstance(other, Vector3D):
            raise ValueError("the input's must be Vector3D Data Type.")
        return Vector3D(
            Number(self.__x1.get() - other[0]),
            Number(self.__x2.get() - other[1]),
            Number(self.__x3.get() - other[2])
        )

    def __mul__(self, scalar):
        """
        Scale the vector by a scalar.
        """
        if not isinstance(scalar, (int, float, Number)):
            raise ValueError("Scalar must be a number (int, float, or Number).")
        if isinstance(scalar, Number):
            scalar = scalar.get()
        return Vector3D(
            Number(self.__x1.get() * scalar),
            Number(self.__x2.get() * scalar),
            Number(self.__x3.get() * scalar)
        )

    def dot(self, other):
        """
        Compute the dot product of two vectors.
        """
        if not isinstance(other, Vector3D):
            raise ValueError("the input's must be Vector3D Data Type.")
        return self.__x1.get() * other[0] + \
               self.__x2.get() * other[1] + \
               self.__x3.get() * other[2]

    def cross(self, other):
        """
        Compute the cross product of two vectors.
        """
        if not isinstance(other, Vector3D):
            raise ValueError("the input's must be Vector3D Data Type.")
        return Vector3D(
            Number(self.__x2.get() * other[2] - self.__x3.get() * other[1]),
            Number(self.__x3.get() * other[0] - self.__x1.get() * other[2]),
            Number(self.__x1.get() * other[1] - self.__x2.get() * other[0])
        )

    def magnitude(self):
        """
        Calculate the magnitude (length) of the vector.
        """
        from math import sqrt
        return sqrt(self.__x1.get()**2 + self.__x2.get()**2 + self.__x3.get()**2)

    def normalize(self):
        """
        Normalize the vector (convert it to a unit vector).
        """
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return Vector3D(
            Number(self.__x1.get() / mag),
            Number(self.__x2.get() / mag),
            Number(self.__x3.get() / mag)
        )

    #let's add some static methods .
    @staticmethod
    def zeros():
        return Vector3D(Number(0),Number(0),Number(0))
    @classmethod
    def ones(cls):
        return cls(Number(1),Number(1),Number(1))
    @staticmethod
    def fill(x):
        return Vector3D(Number(x),Number(x),Number(x))
    @staticmethod
    def unit(direction):
        direction = direction.upper()
        if direction=='X':
            return Vector3D(Number(1),Number(0),Number(0))
        elif direction=='Y':
            return Vector3D(Number(0),Number(1),Number(0))
        elif direction=='Z':
            return Vector3D(Number(0),Number(0),Number(1))
        else :
            raise ValueError("enter valied input x,y,z")


class Tensor:
    def __init__(self, data):
        """
        Initialize the Tensor with nested list data.
        Validates uniform shape and computes it.
        """
        self.__data = data
        self.shape = Tensor.Shape(data)

    @staticmethod
    def Shape(lista):
        """
        Compute the shape of a nested list (e.g. (2, 3), (2, 3, 4), etc.)
        Ensures the structure is uniform (not jagged).
        """
        if isinstance(lista, list) and lista and isinstance(lista[0], list):
            check = []
            for i, item in enumerate(lista):
                if not isinstance(item, list):
                    raise TypeError(f"Item at index {i} is not a list")
                check.append(len(item))
            if len(set(check)) != 1 and len(check) > 1:
                raise IndexError("Inconsistent sublist lengths")

        shape = []
        while isinstance(lista, list):
            shape.append(len(lista))
            if not lista:
                break
            lista = lista[0]
        return tuple(shape)

    @classmethod
    def ones(cls, shape):
        """
        Create a Tensor filled with 1s using nested loops for up to 3D.
        """
        return cls._build_fill(shape, value=1)

    @classmethod
    def zeros(cls, shape):
        """
        Create a Tensor filled with 0s using nested loops for up to 3D.
        """
        return cls._build_fill(shape, value=0)

    @classmethod
    def _build_fill(cls, shape, value):
        """
        Helper method to create tensor with a specific fill value.
        Only supports up to 3D with nested loops.
        """
        if not isinstance(shape, tuple):
            raise TypeError("Shape must be a tuple")

        if len(shape) == 1:
            return cls([value] * shape[0])

        elif len(shape) == 2:
            rows, cols = shape
            return cls([[value for _ in range(cols)] for _ in range(rows)])

        elif len(shape) == 3:
            d1, d2, d3 = shape
            result = []
            for i in range(d1):
                level2 = []
                for j in range(d2):
                    level3 = []
                    for k in range(d3):
                        level3.append(value)
                    level2.append(level3)
                result.append(level2)
            return cls(result)

        else:
            raise NotImplementedError("Only supports up to 3D tensors")

    def get_shape(self):
        return self.shape

    def get_data(self):
        return self.__data

    def __str__(self):
        from pprint import pformat
        return f"Tensor(shape={self.shape})\n{pformat(self.__data)}"

    # -----------------------------
    # Operator overloading
    # -----------------------------

    def __validate_shape_match(self, other):
        if not isinstance(other, Tensor):
            raise TypeError("Operand must be a Tensor")
        if self.shape != other.shape:
            raise ValueError("Shapes do not match for operation")

    def __elementwise_op(self, a, b, op):
        if isinstance(a, list):
            return [self.__elementwise_op(x, y, op) for x, y in zip(a, b)]
        else:
            return op(a, b)

    def __add__(self, other):
        self.__validate_shape_match(other)
        return Tensor(self.__elementwise_op(self.__data, other.__data, lambda x, y: x + y))

    def __sub__(self, other):
        self.__validate_shape_match(other)
        return Tensor(self.__elementwise_op(self.__data, other.__data, lambda x, y: x - y))

    def __mul__(self, other):
        self.__validate_shape_match(other)
        return Tensor(self.__elementwise_op(self.__data, other.__data, lambda x, y: x * y))
        


# In[ ]:



