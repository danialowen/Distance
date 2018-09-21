# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 09:42:40 2018

@author: gydwo
"""

"""File for computing minimum distance between points"""


import math


def compute_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2
                     + (point1[1] - point2[1])**2)
    
point1 = (0, 0)
point2 = (1, 1)

print(compute_distance(point1, point2))
