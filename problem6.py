__author__ = 'darryl'


def sum_of_squares(maxrange):
    return sum([i ** 2 for i in range(1, maxrange + 1)])


def squares_of_sum(maxrange):
    return sum([i for i in range(1, maxrange + 1)]) ** 2


def main():
    print(squares_of_sum(100) - sum_of_squares(100))


if __name__ == '__main__':
    main()
