#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    length = list_length
    i = 0
    while i < length:
        div = 0
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except (ZeroDivisionError, ValueError):
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(div)
        i += 1
    return new_list
