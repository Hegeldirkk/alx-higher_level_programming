#!/usr/bin/python3
if __name__ == "__main__":
    import sys as py
    from calculator_1 import add, sub, mul, div
    operator = ['+', '-', '*', '/']
    a = int(py.argv[1])
    b = int(py.argv[3])
    if len(py.argv) < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        py.exit(1)
    elif operator[0] == py.argv[2]:
        print("{} {} {} = {}".format(py.argv[1], py.argv[2], py.argv[3], a + b))
    elif operator[1] == py.argv[2]:
        print("{} {} {} = {}".format(py.argv[1], py.argv[2], py.argv[3], a - b))
    elif operator[2] == py.argv[2]:
        print("{} {} {} = {}".format(py.argv[1], py.argv[2], py.argv[3], a * b))
    elif operator[3] == py.argv[2]:
        print("{} {} {} = {}".format(py.argv[1], py.argv[2], py.argv[3], a / b))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        py.exit(1)
