
def area(a):
    '''
    Возвращает площаль квадрата со стороной длины a

        Параметры:
            a (int или float): положительное число обозначающее длину стороны квадрата

        Возвращаемое значение:
            a * a (int или float): площадь квадрата со стороной длины a
    '''
    return a * a


def perimeter(a):
    '''
    Возвращает периметр квадрата со стороной длины a

        Параметры:
            a (int или float): положительное число обозначающее длину стороны квадрата

        Возвращаемое значение:
            4 * a (int или float): периметр квадрата со стороной длины a
    '''
    return 4 * a

import unittest

class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
       res = area(0)
       self.assertEqual(res, 0)

    def test_zero_perim(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_normal_area(self):
       res = area(10)
       self.assertEqual(res, 100)

    def test_normal_perim(self):
        res = perimeter(10)
        self.assertEqual(res, 40)

    def test_negative_inputs(self):
        res = area(-5)
        self.assertEqual(res, 25)

        res = perimeter(-6)
        self.assertEqual(res, -24)

    def test_real_inputs(self):
        res = area(1.2)
        self.assertEqual(res, 1.44)

        res = perimeter(1.2)
        self.assertEqual(res, 4.8)

