# -*- coding: utf-8 -*-


def Main():
    class A:
        def __init__(self):
            self.x = 2
    a = A()
    a.x = 1
    print(a.x)


if __name__ == "__main__":
    Main()
