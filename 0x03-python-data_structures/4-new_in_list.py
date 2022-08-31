#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    for i in my_list:
        if idx == my_list.index(i):
            new_list = my_list[:]
            new_list[idx] = element
            return (new_list)
    return (my_list)
