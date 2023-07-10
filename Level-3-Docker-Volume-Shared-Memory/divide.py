# divide.py: takes inline input from the commandline and reads persisted data and divides one by the other
# author: mdeshp10
import sys

file_name='/db/divide_result.txt'

def read_file_content():
    try:
        with open(file_name, 'r') as file_reader:
            result = int(file_reader.read().strip())
    except FileNotFoundError:
        result = 100
    return result

def write_file_content(result):
    with open(file_name, 'w') as file_writer:
        file_writer.write(str(result))

def divide(int1):
    result = read_file_content()
    result = result//int1
    write_file_content(result)
    
    return result

if __name__ == "__main__":
    int1 = int(sys.argv[1])
    result = divide(int1)
    print(result)
