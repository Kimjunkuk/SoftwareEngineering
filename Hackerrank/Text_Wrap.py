
"""
Understanding of text-wrap method

difference between fill() and wrap()

"""

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, width=int(max_width))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

