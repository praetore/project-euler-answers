from euler_utils import is_prime, timeit

__author__ = 'darryl'


def yield_primes():
    yield 2
    result = 3
    while True:
        if is_prime(result):
            yield result
        result += 2


def get_prime_no(number):
    gen = yield_primes()
    i = 0
    while i < number:
        res = next(gen)
        if i + 1 == number:
            print("%dth prime number is %d" % (number, res))
        i += 1


@timeit
def main():
    get_prime_no(10001)


if __name__ == '__main__':
    main()