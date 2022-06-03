#!/usr/bin/python3
if __name__ == "__main__":
    import sys as py
    from calculator_1 import add, sub, mul, div
    operator = ['+', '-', '*', '/']
    if len(py.argv) < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        py.exit(1)
    elif operator[0] != py.argv[2] and operator[1] != py.argv[2] and operator[2] != py.argv[2] and operator[3] != py.argv[2]:
        print("Unknown operator. Available operators: +, -, * and /")
        py.exit(1)
    else:
        print("{} {} {} = {}".format(py.argv[1], py.argv[2], py.argv[3], int(py.argv[1] + py.argv[3])))
