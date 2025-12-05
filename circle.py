import math


def area(r):
    '''
    Возвращает площадь круга с радиусом r

        Параметры:
            r (int или float): положительное число обозначающее длину радиуса круга

        Возвращаемое значение:
            math.pi * r * r (float): площадь круга с радиусом длины r
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает периметр круга с радиусом r

    Параметры:
        r (int или float): положительное число обозначающее длину радиуса круга

    Возвращаемое значение:
        2 * math.pi * r (float): периметр круга с радиусом длины r
    '''
    return 2 * math.pi * r

import unittest

class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
       res = area(0)
       self.assertEqual(res, 0)

    def test_zero_perim(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_normal_area(self):
       res = area(10)
       self.assertEqual(res, 314.1592653589793)

    def test_normal_perim(self):
        res = perimeter(10)
        self.assertEqual(res, 62.83185307179586)

    def test_negative_inputs(self):
        res = area(-5)
        self.assertEqual(res, 78.53981633974483)

        res = perimeter(-6)
        self.assertEqual(res, -37.69911184307752)

