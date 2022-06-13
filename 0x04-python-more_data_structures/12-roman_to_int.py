#!/usr/bin/python3
def roman_to_int(roman_string):
    num = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    n = 0
    total = 0
    if isinstance(roman_string, str):
        for n in range(len(roman_string) - 1):
            if num[roman_string[n]] >= num[roman_string[n + 1]]:
                total += num[roman_string[n]]
            else:
                total -= num[roman_string[n]]
            n += 1
        total += num[roman_string[n]]
        return total
    return 0
