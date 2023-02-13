# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
        self.assertEqual(classifyTriangle(8,15,17),'Right','8,15,17 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        self.assertEqual(classifyTriangle(5,12,13),'Right','5,12,13 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertEqual(classifyTriangle(4,4,4),'Equilateral','4,4,4 is a Equilateral triangle')

    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(5,10,14),'Scalene','5,10,4 is a Scalene triangle')
        self.assertEqual(classifyTriangle(6,5,4),'Scalene','6,5,4 is a Scalene triangle')
    def testIsocelesTriangle(self):
       # self.assertEqual(classifyTriangle(4,4,6),'Isoceles','4,5,4 is a Isoceles triangle')
        self.assertEqual(classifyTriangle(5,5,4),'Isoceles','5,5,4 is a Isoceles triangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

