
"""
arr[::-1] arr의 배열을 거꾸로 출력하도록 한다. 
* << 양옆에 함께 출력되는 []<< 특수문자 없이 출력되도록 한다.

"""

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    print(*arr[::-1])
    
