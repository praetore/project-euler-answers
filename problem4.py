"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
from collections import deque
from euler_utils import timeit

__author__ = 'Darryl'


def largest_palindrome(max_num):
    largest = 0
    for i in range(max_num):
        to_check = set(range(max_num)).difference(range(i))
        for x in to_check:
            if is_palindrome(i*x) and i*x > largest:
                largest = i*x
    return largest


def is_palindrome(num):
    nums = list(str(num))
    de = deque(nums)
    while len(de) > 1:
        if de.pop() != de.popleft():
            return False
    return True


@timeit
def main():
    print(largest_palindrome(1000))


if __name__ == '__main__':
    main()