"""
round(float value, index number)
"""


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
    total=0
    tip= float(meal_cost)*(tip_percent/100)
    tax=float(meal_cost)*(tax_percent/100)
    total=float(meal_cost)+tip+tax
    return print(int(round(total,0)))

if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
