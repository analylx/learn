#!/bin/python3


def solve(s):
    a = s.split(' ')
    return " ".join(word.capitalize() for word in a)


if __name__ == '__main__':
    s = input()
    print(solve(s))
