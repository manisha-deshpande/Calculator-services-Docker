# plus.py: takes inline input from the commandline and adds two numbers
# author: manisha-deshpande
import sys

def plus(int1, int2):
    return int1 + int2

if __name__ == "__main__":
    if(len(sys.argv) == 3):
        int1 = int(sys.argv[1])
        int2 = int(sys.argv[2])
    else:
        int1 = int(input())
        int2 = int(sys.argv[1])

    result = plus(int1, int2)
    print(result)
