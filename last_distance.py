# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 11:39:49 2018

@author: gydwo
"""

"""
Test for distance.py
"""


import math
from distance import compute_distance, compute_minimum_distance

def test_compute_distance():
    point1 = (0, 0)
    point2 = (1, 1)
    assert(compute_distance(point1, point2) == math.sqrt(2))
    assert(compute_distance(point1, point1) == 0)

def test_compute_minimum_distance():
    point1 = (0, 0)
    point2 = (1, 1)
    point3 = (1, 0)
    list_of_points = [point1, point2, point3]
    assert(compute_minimum_distance(list_of_points) == 1)
    
    
import pytest
pytest.main()