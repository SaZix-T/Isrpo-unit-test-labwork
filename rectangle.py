def area(a, b): 
    return a * b 

def perimeter(a, b): 
    return a + b 


import unittest

class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
       res = area(10, 0)
       self.assertEqual(res, 0)

    def test_zero_perim(self):
        res = perimeter(10, 0)
        self.assertEqual(res, 10)

    def test_square_area(self):
       res = area(10, 10)
       self.assertEqual(res, 100)

    def test_square_perim(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 20)

    def test_negative_inputs(self):
        res = area(-5, -6)
        self.assertEqual(res, 30)

        res = perimeter(-5, -6)
        self.assertEqual(res, -11)

