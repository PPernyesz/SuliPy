import math
import os
import random
import re
import sys



if __name__ == '__main__':
    print("Write a number: ")
    n = int(input().strip())
    
    if (n%2!=0) or (n>=6 and n<=20):
        print("Weird")
    else:
        if (n>=2 and n<=5) or (n>20):
            print("Not Weird")