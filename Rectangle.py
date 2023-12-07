#!/usr/bin/env python
# coding: utf-8

# In[4]:


import matplotlib.pyplot as plt
import numpy as np

class Rectangle:
    def __init__(self, left_bottom, right_up):
        self.left_bottom = left_bottom
        self.right_up = right_up

    def area(self):
        width = self.right_up[0] - self.left_bottom[0]
        height = self.right_up[1] - self.left_bottom[1]
        return width * height

    def perimeter(self):
        width = self.right_up[0] - self.left_bottom[0]
        height = self.right_up[1] - self.left_bottom[1]
        return 2 * (width + height)

    def __str__(self):
        return f"Rectangle;Left-Bottom:{self.left_bottom};Right-Up:{self.right_up};None;None"

    def graphFigure(self):
        x = [self.left_bottom[0], self.right_up[0], self.right_up[0], self.left_bottom[0], self.left_bottom[0]]
        y = [self.left_bottom[1], self.left_bottom[1], self.right_up[1], self.right_up[1], self.left_bottom[1]]

        plt.figure()
        plt.plot(x, y, label='Rectangle', marker='o')
        plt.title('Rectangle')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.legend()
        plt.grid(True)
        plt.show()
        
    @classmethod
    def constructFromSeries(cls, series):
        left_bottom = tuple(map(float, series[1].split(':')))
        right_up = tuple(map(float, series[2].split(':')))
        return cls(left_bottom, right_up)

"""    
# Пример использования:
left_bottom_rectangle = (12, 12)
right_up_rectangle = (14, 16)

rectangle = Rectangle(left_bottom_rectangle, right_up_rectangle)
print(f"Area: {rectangle.area()}")
print(f"Perimeter: {rectangle.perimeter()}")
print(f"String Representation: {rectangle}")
rectangle.graphFigure()
"""


# In[ ]:




