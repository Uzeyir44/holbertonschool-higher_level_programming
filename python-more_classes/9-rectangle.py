#!/usr/bin/python3
"""
This module contains class Rectangle
"""


class Rectangle:
    """
    This class represents a rectangle

    Attributes:
        width (int): private attribute representing the width
        height (int): private attribute representing the height

    Methods:
        area (int): returns the area
        perimeter (int): returns the perimeter
        bigger_or_equal (Rectangle): compares areas of instances
        square (Rectangle): creates new instance with width==height
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        if (type(width) is not int):
            raise TypeError("width must be an integer")
        if (width < 0):
            raise ValueError("width must be >= 0")
        if (type(height) is not int):
            raise TypeError("height must be an integer")
        if (height < 0):
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        This functions serves as getter

        Return:
            self.__width (int): the width of rectangle
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        This function sets new value for width attribute
        """
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        This functions serves as getter

        Return:
            self.__height (int): the width of rectangle
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        This function sets new value for height attribute
        """
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        This function evaluates the area of rectangle

        Return:
            (int): the product of height and width
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """
        This function evaluates the perimeter of rectangle

        Return:
            (int): the double sum of height and width
        """
        if (self.__height == 0 or self.__width == 0):
            return (0)

        return (2 * (self.__width + self.__height))

    def bigger_or_equal(rect_1, rect_2):
        """
        This function compares the areas of two objects

        Return:
            rect_1 (Rectangle): if  rect_1.area() >= rect_2.area()
            rect_2 (Rectangle): if  rect_1.area() < rect_2.area()

        Raises:
            TypeError: if rect_1 or rect_2 is not Rectangle type
        """
        if (type(rect_1) is not Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if (type(rect_2) is not Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if (rect_1.area() >= rect_2.area()):
            return (rect_1)
        else:
            return (rect_2)

    @classmethod
    def square(cls, size=0):
        """
        This function creates new instance of Rectangle class

        Return:
            (Rectangle): new instance with width == height
        """
        width = size
        height = size

        return (cls(width, height))

    def __str__(self):
        if (self.__height == 0 or self.__width == 0):
            return ("")

        temp = ""
        for i in range(self.__height):
            if (i != 0):
                temp += "\n"
            temp += str(self.print_symbol) * self.__width
        return (temp)

    def __repr__(self):
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
