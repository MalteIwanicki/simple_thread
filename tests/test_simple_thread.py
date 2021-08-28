import pytest
from simple_thread.simple_thread import SimpleThread


def return_test():
    return "test"


def test_no_parameter_thread():
    thread = SimpleThread(return_test)
    assert thread.join() == return_test()


def double(number):
    return number * 2


def test_one_parameter_thread():
    number = 2
    thread = SimpleThread(double, (number))
    assert thread.join() == double(number)


def adds_a_and_b(a, b):
    return a + b


def test_two_parameters_thread():
    a = 5
    b = 10
    thread = SimpleThread(adds_a_and_b, (a, b))
    assert thread.join() == adds_a_and_b(a, b)
