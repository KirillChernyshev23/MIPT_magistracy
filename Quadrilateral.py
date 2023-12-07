#!/usr/bin/env python
# coding: utf-8

# In[5]:


import matplotlib.pyplot as plt
import numpy as np

class Quadrilateral:
    def __init__(self, vertices):
        self.vertices = vertices

    def area(self):
        return self.shoelace_formula(self.vertices)

    def perimeter(self):
        perim = 0
        for i in range(3):
            perim += np.linalg.norm(np.array(self.vertices[i]) - np.array(self.vertices[i + 1]))
        perim += np.linalg.norm(np.array(self.vertices[3]) - np.array(self.vertices[0]))
        return perim

    def __str__(self):
        return f"Quadrilateral;{';'.join(map(str, self.vertices))}"

    def graphFigure(self):
        x, y = zip(*self.vertices)

        plt.figure()
        plt.plot(x + (x[0],), y + (y[0],), label='Quadrilateral', marker='o')
        plt.title('Quadrilateral')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.legend()
        plt.grid(True)
        plt.show()

    @staticmethod
    def shoelace_formula(vertices):
        x, y = zip(*vertices)
        return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))

    @classmethod
    def constructFromSeries(cls, series):
        vertices = [tuple(map(float, coord.split(':'))) for coord in series[1:5]]
        return cls(vertices)
"""
# Пример использования:
left_bottom_quadrilateral = (0, 0)
left_top_quadrilateral = (1, 1)
right_up_quadrilateral = (4, 6)
right_bottom_quadrilateral = (3, 2)

quadrilateral = Quadrilateral([left_bottom_quadrilateral, left_top_quadrilateral, right_up_quadrilateral, 
                              right_bottom_quadrilateral])
print(f"Area: {quadrilateral.area()}")
print(f"Perimeter: {quadrilateral.perimeter()}")
print(f"String Representation: {quadrilateral}")
quadrilateral.graphFigure()
"""


# In[ ]:




