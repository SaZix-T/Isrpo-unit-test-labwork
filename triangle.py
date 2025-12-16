def area(a, h): 
    return a * h / 2 

def perimeter(a, b, c): 
    return a + b + c

import unittest

class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
       res = area(10, 0)
       self.assertEqual(res, 0)

    def test_zero_perim(self):
        res = perimeter(0, 10, 0)
        self.assertEqual(res, 10)

    def test_square_area(self):
       res = area(10, 10)
       self.assertEqual(res, 50)

    def test_triple_perim(self):
        res = perimeter(10, 10, 10)
        self.assertEqual(res, 30)

    def test_negative_inputs(self):
        res = area(-5, -6)
        self.assertEqual(res, 15)

        res = perimeter(-5, -6, -7)
        self.assertEqual(res, -18)

    def test_real_inputs(self):
        res = area(1.2, 2.3)
        self.assertEqual(res, 1.38)

        res = perimeter(1.2, 2.3, 3.4)
        self.assertEqual(res, 6.9)

