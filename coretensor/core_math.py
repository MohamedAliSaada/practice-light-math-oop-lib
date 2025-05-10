#!/usr/bin/env python
# coding: utf-8

# In[3]:


from math import gcd,sqrt

# -------------------------------
# Number class: foundational numeric wrapper
# -------------------------------
class Number:
    # This class contains object methods and represents a custom number type.
    # It accepts only int or float values and wraps them with object-oriented behavior.

    def __init__(self, value):
        # We check if the provided value is an int or float using isinstance().
        # It returns True if the value is a number, so we use 'not' to reverse it.
        # If the value fails this check, we raise an error.
        # This allows us to define a new data type (Number) that only wraps real numbers.
        if not isinstance(value, (int, float)):
            raise ValueError('The number must be int or float type')
            
        # If the value passes the check, we store it as a private attribute.
        self.__value = value
        # Since this attribute is private (starts with __), it cannot be accessed or changed directly.
        # So we must provide getter and setter methods to interact with it safely.

    def get(self):
        # Getter method to access the private value from outside the class.
        return self.__value
        
    def set(self, n_value):
        # Setter method to update the private value.
        # Again, we check the type to make sure it's int or float.
        if not isinstance(n_value, (int, float)): 
            raise ValueError('The number must be int or float type')
        self.__value = n_value

    # -------------------------------------
    # Define add and subtract operations
    # And override the __str__ (dunder method) to make printing easier.

    # This method just returns the sum of the stored value and another raw number.
    # Note: The result here is not wrapped in a Number object.
    # This is just for explanation purposes.
    def addR(self, n):
        return self.__value + n

    def add(self, n):
        # Now we want to add another Number object to this one.
        # So we first check if the input 'n' is of type Number.
        if not isinstance(n, Number):
            raise ValueError("It's must be a Number type!")
        
        # Since 'n' is confirmed to be a Number object,
        # we can safely use the .get() method to access its internal value.
        # Like for example: 'saada'.upper() calls the 'upper' method of the str class.
        return Number(self.__value + n.get())

    def sub(self, n):
        # Same logic as in add(): we ensure 'n' is a Number object
        if not isinstance(n, Number):
            raise ValueError("It's must be a Number type!")
        return Number(self.__value - n.get())

    def __str__(self):
        # We override the __str__ method (dunder) to control what is shown when we print the object.
        return f"{self.__value}"


# -------------------------------
# Fraction class: use two Numbers classes
# -------------------------------
# Now we use two Number objects to build a Fraction — this is a bigger building block based on our custom Number data type.
class Fraction:
    def __init__(self, num, den):
        # Check if both numerator and denominator are of type Number (our custom type that wraps int/float)
        # This means Fraction accepts only Number objects — not raw integers or floats.
        if not isinstance(num, Number) or not isinstance(den, Number):
            raise ValueError("The numerator and denominator must be of type Number")

        # Store them as private attributes for encapsulation
        self.__num = num
        self.__den = den

        self.simplify()
        # You could check for division by zero here too (using .get()), like:
        # if self.__den.get() == 0:
        #     raise ZeroDivisionError("Denominator cannot be zero")

    # Since __num and __den are private, we need getter and setter methods to access and update them safely.
    # These attributes are Number objects, so we expect all operations to work with Number.

    def getn(self):
        # Return the numerator (Number object)
        return self.__num

    def getd(self):
        # Return the denominator (Number object)
        return self.__den

    def setn(self, n):
        # Update numerator — only accepts a Number object
        if not isinstance(n, Number):
            raise ValueError("The numerator must be of type Number")
        # This ensures that only a valid Number object can be used to update the numerator.
        self.__num = n

    # EXPLANATION PURPOSE ONLY:
    # This method shows how we *could* allow raw int or float values to be set as numerator
    def setnr(self, n):
        # Accept a raw int or float and convert it into a Number automatically
        if not isinstance(n, (int, float)):
            raise ValueError("The numerator must be int or float")
        self.__num = Number(n)

    def setd(self, d):
        # Update denominator — must also be a Number
        if not isinstance(d, Number):
            raise ValueError("The denominator must be of type Number")
        self.__den = d

    def __str__(self):
        # Display the values inside the Number objects (not the object itself)
        return f"{self.__num.get()}/{self.__den.get()}"

    # -----------------------------------------
    # Now let's add some fraction functions
    # But first, remember we can create Number like: v = Number(10)
    # And we can add two Numbers either by using .add() or using .get() and native +
    # Because we made the value private inside Number, we must use .get() to access it for math
    # -----------------------------------------

    def add(self, other_fraction):
        # First check: must be a Fraction object
        if not isinstance(other_fraction, Fraction):
            raise ValueError("Argument must be of type Fraction")

        # Extract Number objects for numerator and denominator
        n1 = other_fraction.getn()
        d1 = other_fraction.getd()

        # Use raw numbers with .get() to apply the formula:
        # (a*d + b*c) / (b*d)
        a = self.__num.get()
        b = self.__den.get()
        c = n1.get()
        d = d1.get()

        new_num = Number(a * d + b * c)
        new_den = Number(b * d)

        return Fraction(new_num, new_den)

    def sub(self, other_fraction):
        # Same steps as add, but use subtraction in the formula
        if not isinstance(other_fraction, Fraction):
            raise ValueError("Argument must be of type Fraction")

        n1 = other_fraction.getn()
        d1 = other_fraction.getd()

        a = self.__num.get()
        b = self.__den.get()
        c = n1.get()
        d = d1.get()

        new_num = Number(a * d - b * c)
        new_den = Number(b * d)

        return Fraction(new_num, new_den)

    def mul(self, other_fraction):
        # Multiplication of fractions: (a/b) * (c/d) = (a*c) / (b*d)
        if not isinstance(other_fraction, Fraction):
            raise ValueError("Argument must be of type Fraction")

        a = self.__num.get()
        b = self.__den.get()
        c = other_fraction.getn().get()
        d = other_fraction.getd().get()

        new_num = Number(a * c)
        new_den = Number(b * d)

        return Fraction(new_num, new_den)

    def div(self, other_fraction):
        # Division of fractions: (a/b) ÷ (c/d) = (a*d) / (b*c)
        if not isinstance(other_fraction, Fraction):
            raise ValueError("Argument must be of type Fraction")
        if other_fraction.getn().get() == 0:
            raise ZeroDivisionError("Cannot divide by a fraction with numerator = 0")

        a = self.__num.get()
        b = self.__den.get()
        c = other_fraction.getn().get()
        d = other_fraction.getd().get()

        new_num = Number(a * d)
        new_den = Number(b * c)

        return Fraction(new_num, new_den)


    def simplify(self):    #call at init to work automatic with each run to fraction
        # Simplify the fraction using GCD (greatest common divisor) 
        a = int(self.__num.get())
        b = int(self.__den.get())
        g = gcd(a, b)

        # Only simplify if GCD is not 0 or 1
        if g > 1:
            self.__num.set(a // g)
            self.__den.set(b // g)


# -------------------------------------------
# Vector2D class: A 2D vector built using two Number objects (x, y)
# -------------------------------------------
class Vector2D:
    def __init__(self, x, y):
        # Make sure both x and y are Number objects
        if not isinstance(x, Number) or not isinstance(y, Number):
            raise ValueError("Both x and y must be of type Number")
        self.__x = x
        self.__y = y

    # Getter methods
    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    # Setter methods
    def setx(self, n_x):
        if not isinstance(n_x, Number):
            raise ValueError("x must be a Number")
        self.__x = n_x

    def sety(self, n_y):
        if not isinstance(n_y, Number):
            raise ValueError("y must be a Number")
        self.__y = n_y

    # Print vector as [ x , y ]
    def __str__(self):
        return f"[ {self.__x.get()} , {self.__y.get()} ]"

    # --------------------------------------------
    # Vector addition: [x1, y1] + [x2, y2] = [x1+x2, y1+y2]
    def add(self, other):
        if not isinstance(other, Vector2D):
            raise ValueError("Argument must be a Vector2D")
        
        new_x = Number(self.__x.get() + other.getx().get())
        new_y = Number(self.__y.get() + other.gety().get())

        return Vector2D(new_x, new_y)

    # --------------------------------------------
    # Vector subtraction: [x1, y1] - [x2, y2] = [x1-x2, y1-y2]
    def sub(self, other):
        if not isinstance(other, Vector2D):
            raise ValueError("Argument must be a Vector2D")
        
        new_x = Number(self.__x.get() - other.getx().get())
        new_y = Number(self.__y.get() - other.gety().get())

        return Vector2D(new_x, new_y)

    # --------------------------------------------
    # Dot product: x1*x2 + y1*y2 → returns a Number
    def dot(self, other):
        if not isinstance(other, Vector2D):
            raise ValueError("Argument must be a Vector2D")

        x1 = self.__x.get()
        y1 = self.__y.get()
        x2 = other.getx().get()
        y2 = other.gety().get()

        result = x1 * x2 + y1 * y2
        return Number(result)

    # --------------------------------------------
    # Magnitude: sqrt(x^2 + y^2) → returns float
    def magnitude(self):
        x = self.__x.get()
        y = self.__y.get()
        return sqrt(x**2 + y**2)


# In[ ]:





# In[ ]:



