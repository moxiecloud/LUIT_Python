
#!/bin/python

import math
import os
import random
import re
import sys

def process_num(n):
    if (n % 2) != 0:
        print("Weird")
    elif ((n % 2) == 0) and range(2,5):
        print("Not Weird")
    elif ((n % 2) == 0) and range(6,20):
        print("Weird")
    elif ((n % 2) == 0) and n > 20:
        print("Not Weird")
    else:
        pass


if __name__ == '__main__':
    n = int(raw_input().strip())
    if not(1 <= n <= 100):
        print("You need to enter a number between 1 and 100. ")
    else:
        process_num(n)
