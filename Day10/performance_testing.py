from timeit import timeit, Timer


def time_single_expressions():
    timer_xor_swap = Timer('a^=b;b^=a;a^=b', setup='a, b = 1, 2')
    timer_temp_swap = Timer('t=a;a=b;b=t', setup='a, b = 1, 2')
    timer_tuple_swap = Timer('a,b=b,a', setup='a, b = 1, 2')
    print('XOR ', timer_xor_swap.timeit())
    print('TEMP ', timer_temp_swap.timeit())
    print('TUPLE ', timer_tuple_swap.timeit())


def test():
    """A function to test"""
    L = [i for i in range(100)]


if __name__ == '__main__':
    print(timeit("test()", setup="from __main__ import test"))
    time_single_expressions()
