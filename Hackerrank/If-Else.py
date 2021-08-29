#!/bin/python3

import math
import os
import random
import re
import sys

"""
Natural Language
If n is odd, print Weird
If n is even and in the inclusive range of  to , print Not Weird
If n is even and in the inclusive range of  to , print Weird
If n is even and greater than , print Not Weird

Whole range : 1- 100

짝수인데 5보다 작거나 20보다 크면 Not Weird
나머지  "Weird"  

 
Pseudo-code
n<=5 or 20>n and n%2==0
print("Not Weird")
else 
("Weird")

"""


if __name__ == '__main__':
    n = int(input().strip())
    
    if n%2==0 and (n<=5 or n>20): 
        print("Not Weird") 
    else :
        print("Weird")
    
    

