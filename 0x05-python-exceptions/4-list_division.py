#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for n in range(0, list_length):
        try:
            result_l = my_list_1[n] / my_list_2[n]
        except TypeError:
            print("wrong type")
            result_l = 0
        except ZeroDivisionError:
            print("division by 0")
            result_l = 0
        except IndexError:
            print("out of range")
            result_l = 0
        finally:
            new_list.append(result_l)
    return new_list
