import random
import sys
import os
import time
import entity_data
import entity
import re
from main import confirmation_check

def main() -> None:
    test_string = 'This is a sentence to try and test altering text writing speeds!'
    empty_string = ''
    # os.system('cls') # \033[A\033[A would also clear but something of it going up one in the terminal line
    for char in test_string:
        # empty_string += char
        print(char, end ='', flush=True)
        time.sleep(0.064)
        # if len(empty_string) != len(test_string):
        #     os.system('cls')

if __name__ == '__main__':
    main()