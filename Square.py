#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
import numpy as np

class Square:
    def __init__(self, left_bottom, side_length):
        self.left_bottom = left_bottom
        self.side_length = side_length

    def area(self):
        return self.side_length**2

    def perimeter(self):
        return 4 * self.side_length

    def __str__(self):
        return f"Square;Left-Bottom:{self.left_bottom};Side-Length:{self.side_length};None;None"

    def graphFigure(self):
        x = [self.left_bottom[0], self.left_bottom[0] + self.side_length, 
             self.left_bottom[0] + self.side_length, self.left_bottom[0], self.left_bottom[0]]
        y = [self.left_bottom[1], self.left_bottom[1], 
             self.left_bottom[1] + self.side_length, self.left_bottom[1] + self.side_length, self.left_bottom[1]]

        plt.figure()
        plt.plot(x, y, label='Square', marker='o')
        plt.title('Square')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.legend()
        plt.grid(True)
        plt.axis('equal')
        plt.show()

"""
# Пример использования:
left_bottom_square = (9, 17)
side_length_square = 4.5

square = Square(left_bottom_square, side_length_square)
print(f"Area: {square.area()}")
print(f"Perimeter: {square.perimeter()}")
print(f"String Representation: {square}")
square.graphFigure()
"""


# In[ ]:




