"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
from fractions import gcd
from functools import reduce
from euler_utils import timeit

__author__ = 'Darryl'


def lcm(a, b):
    return a * b // gcd(a, b)


def lcmm(*args):
    return reduce(lcm, *args)


@timeit
def main():
    print(lcmm(range(1, 21)))


if __name__ == '__main__':
    main()