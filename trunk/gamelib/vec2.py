
from __future__ import division
from math import atan2, sqrt
import operator


class Vec2(object):

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Vec2(%s, %s)' % (self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vec2(self.x * scalar, self.y * scalar)

    __rmul__ = __mul__

    def __floordiv__(self, scalar):
        return Vec2(self.x // scalar, self.y // scalar)

    def __rfloordiv__(self, scalar):
        return Vec2(scalar // self.x, scalar // self.y)

    def __truediv__(self, scalar):
        return Vec2(self.x / scalar, self.y / scalar)

    def __rtruediv__(self, scalar):
        return Vec2(scalar / self.x, scalar / self.y)

    def __div__(self, scalar):
        return Vec2(
            operator.div(self.x, scalar),
            operator.div(self.y, scalar),
        )

    def __rdiv__(self, scalar):
        return Vec2(
            operator.div(scalar, self.x),
            operator.div(scalar, self.y),
        )

    def __idiv__(self, scalar):
        self.x = operator.div(self.x, scalar)
        self.y = operator.div(self.y, scalar)

    @property
    def angle(self):
        if self.x == 0 and self.y ==0:
            raise ZeroDivisionError('Vec2(0, 0) has no angle')
        return atan2(self.y, self.x)

    @property
    def length(self):
        return sqrt(self.x * self.x + self.y * self.y)

    def normalize(self):
        length = self.length
        self.x /= length
        self.y /= length

    def normalized(self):
        length = self.length
        return Vec2(self.x / length, self.y / length)

    def dot(self, other):
        return (self.x * other.x + self.y * other.y)

