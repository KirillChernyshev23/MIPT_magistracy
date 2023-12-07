#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def area(self):
        return np.pi * self.radius**2

    def perimeter(self):
        return 2 * np.pi * self.radius

    def __str__(self):
        return f"Circle;Center:{self.center};Radius:{self.radius};None;None"

    def graphFigure(self):
        theta = np.linspace(0, 2 * np.pi, 100)
        x = self.center[0] + self.radius * np.cos(theta)
        y = self.center[1] + self.radius * np.sin(theta)

        plt.figure()
        plt.plot(x, y, label='Circle')
        plt.scatter(*self.center, color='red', label='Center')
        plt.title('Circle')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.legend()
        plt.grid(True)
        plt.axis('equal')
        plt.show()
        
    @classmethod
    def constructFromSeries(cls, series):
        center = tuple(map(float, series[1].split(':')))
        radius = float(series[2])
        return cls(center, radius)
    
"""
# Пример использования:
center_circle = (0, 0)
radius_circle = 10

circle = Circle(center_circle, radius_circle)
print(f"Area: {circle.area()}")
print(f"Perimeter: {circle.perimeter()}")
print(f"String Representation: {circle}")
circle.graphFigure()
"""

