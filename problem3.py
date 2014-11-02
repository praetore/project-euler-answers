"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
from euler_utils import timeit

__author__ = 'Darryl'


@timeit
def main():
    number = 600851475143
    div = 3
    while number / div > 1:
        if not number % div:
            number /= div
        div += 2
    print(div)


if __name__ == '__main__':
    main()