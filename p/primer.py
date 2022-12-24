#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def mul(a):
    def helper(b):
        return a * b

    return helper


def fun1(a):
    x = a * 3

    def fun2(b):
        nonlocal x
        return b + x

    return fun2


if __name__ == '__main__':
    print("ex1\n", mul(5)(2))

    test_fun = fun1(4)
    print("ex2\n", test_fun(7))
