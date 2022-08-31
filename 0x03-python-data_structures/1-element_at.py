#!/usr/bin/python3
def element_at(my_list, idx):
    for i in my_list:
        if idx == my_list.index(i):
            return (i)
    return (None)
