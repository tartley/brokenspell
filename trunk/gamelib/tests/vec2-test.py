
from __future__ import division
from math import pi
import operator

from unittestplus.testcaseplus import TestCasePlus
from unittestplus.run import run

from ..vec2 import Vec2


class Vec2Test(TestCasePlus):

    def test_init0(self):
        vec2 = Vec2()
        self.assertEquals(vec2.x, 0.0)
        self.assertEquals(vec2.y, 0.0)

    def test_init2(self):
        vec2 = Vec2(2, 3)
        self.assertEquals(vec2.x, 2)
        self.assertEquals(vec2.y, 3)

    def test_str(self):
        self.assertEquals(str(Vec2(3, 4)), 'Vec2(3, 4)')

    def test_eq(self):
        self.assertTrue(Vec2(2, 3) == Vec2(2, 3))
        self.assertFalse(Vec2(2, 3) == Vec2(0, 3))
        self.assertFalse(Vec2(2, 3) == Vec2(2, 0))

    def test_ne(self):
        self.assertFalse(Vec2(2, 3) != Vec2(2, 3))
        self.assertTrue(Vec2(2, 3) != Vec2(0, 3))
        self.assertTrue(Vec2(2, 3) != Vec2(2, 0))

    def test_add(self):
        a = Vec2(20, 30)
        b = Vec2(2, 3)
        self.assertEquals(a + b, Vec2(22, 33))

    def test_sub(self):
        a = Vec2(22, 33)
        b = Vec2(2, 3)
        self.assertEquals(a - b, Vec2(20, 30))

    def test_iadd(self):
        a = Vec2(20, 30)
        b = Vec2(2, 3)
        a += b
        self.assertEquals(a, Vec2(22, 33))

    def test_isub(self):
        a = Vec2(22, 33)
        b = Vec2(2, 3)
        a -= b
        self.assertEquals(a, Vec2(20, 30))

    def test_mul(self):
        a = Vec2(3, 4)
        self.assertEquals(a * 10, Vec2(30, 40))
        self.assertEquals(10 * a, Vec2(30, 40))
        self.assertEquals(a, Vec2(3, 4))

    def test_imul(self):
        a = Vec2(3, 4)
        a *= 10
        self.assertEquals(a, Vec2(30, 40))

    def test_div(self):
        a = Vec2(31, 41)
        self.assertEquals(operator.div(a, 10), Vec2(3, 4))
        self.assertEquals(operator.div(10, a), Vec2(10 // 31, 10 // 41))
        self.assertEquals(a, Vec2(31, 41))

    def test_idiv(self):
        a = Vec2(31, 41)
        operator.idiv(a, 10)
        self.assertEquals(a, Vec2(3, 4))

    def test_truediv(self):
        a = Vec2(31, 41)
        self.assertEquals(operator.truediv(a, 10), Vec2(3.1, 4.1))
        self.assertEquals(operator.truediv(10, a), Vec2(10 / 31, 10 / 41))
        self.assertEquals(a, Vec2(31, 41))

    def test_itruediv(self):
        a = Vec2(31, 41)
        a /= 10
        self.assertEquals(a, Vec2(3.1, 4.1))

    def test_floordiv(self):
        a = Vec2(31, 41)
        self.assertEquals(operator.floordiv(a, 10), Vec2(3, 4))
        self.assertEquals(operator.floordiv(10, a), Vec2(10 // 31, 10 // 41))
        self.assertEquals(a, Vec2(31, 41))

    def test_ifloordiv(self):
        a = Vec2(31, 41)
        a //= 10
        self.assertEquals(a, Vec2(3, 4))

    def test_angle(self):
        self.assertEquals(Vec2(1, 0).angle, 0.0)
        self.assertEquals(Vec2(1, 1).angle, pi/4)
        self.assertEquals(Vec2(0, 1).angle, pi/2)
        self.assertEquals(Vec2(-1, 0).angle, pi)
        self.assertEquals(Vec2(-1, -1).angle, -3*pi/4)

    def test_angle_zero(self):
        v = Vec2(0, 0)
        self.assertRaises(lambda: v.angle, ZeroDivisionError)

    def test_length(self):
        self.assertEquals(Vec2(0, 0).length, 0.0)
        self.assertEquals(Vec2(3, 0).length, 3.0)
        self.assertEquals(Vec2(0, 4).length, 4.0)
        self.assertEquals(Vec2(3, 4).length, 5.0)

    def test_normalize(self):
        v = Vec2(3, 4)
        self.assertEquals(v.normalize(), None)
        self.assertEquals(v, Vec2(3 / 5, 4 / 5))

    def test_normalized(self):
        v = Vec2(3, 4)
        self.assertEquals(v.normalized(), Vec2(3 / 5, 4 / 5))
        self.assertEquals(v, Vec2(3, 4))

    def test_normalize_zero(self):
        v = Vec2(0, 0)
        self.assertRaises(v.normalize, ZeroDivisionError)
        self.assertRaises(v.normalized, ZeroDivisionError)

    def test_dot(self):
        a = Vec2(3, 4)
        self.assertEquals(a.dot(a), 25)
        self.assertEquals(a.dot(Vec2(4, -3)), 0)


if __name__ == '__main__':
    run(Vec2Test)

