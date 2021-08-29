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

If n is odd print "Weird"  
If n even and in range between 2 and 5 print "Not Weird" 
 
Pseudo-code
if 2 <= n <= 5 / 2 == 0
print("Not Weird")
else 
("Weird")

"""

if __name__ == '__main__':
    n = int(input().strip())
    
    if (2<=n<=5)/2==0:
        print("Not Weird")
    else :
        print("Weird")
    

