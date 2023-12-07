#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
import numpy as np

class Ellipse:
    def __init__(self, center, a_axis, b_axis):
        self.center = center
        self.a_axis = a_axis
        self.b_axis = b_axis

    def area(self):
        return np.pi * self.a_axis * self.b_axis

    def perimeter(self):
        # Использую приближенную формулу для вычисления периметра эллипса
        h = ((self.a_axis - self.b_axis) ** 2) / ((self.a_axis + self.b_axis) ** 2)
        return np.pi * (self.a_axis + self.b_axis) * (1 + (3 * h) / (10 + np.sqrt(4 - 3 * h)))

    def __str__(self):
        return f"Ellipse;Center:{self.center};A-axis:{self.a_axis};B-axis:{self.b_axis};None"

    def graphFigure(self):
        theta = np.linspace(0, 2 * np.pi, 100)
        x = self.center[0] + self.a_axis * np.cos(theta)
        y = self.center[1] + self.b_axis * np.sin(theta)

        plt.figure()
        plt.plot(x, y, label='Ellipse')
        plt.scatter(*self.center, color='red', label='Center')
        plt.title('Ellipse')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.legend()
        plt.grid(True)
        plt.show()
        
    @classmethod
    def constructFromSeries(cls, series):
        center = tuple(map(float, series[1].split(':')))
        a_axis = float(series[2])
        b_axis = float(series[3])
        return cls(center, a_axis, b_axis)
"""    
# Пример использования:
center = (6, 6)
a_axis = 10
b_axis = 3

ellipse = Ellipse(center, a_axis, b_axis)
print(f"Area: {ellipse.area()}")
print(f"Perimeter: {ellipse.perimeter()}")
print(f"String Representation: {ellipse}")
ellipse.graphFigure()    
"""


# In[ ]:




