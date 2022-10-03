#!/usr/bin/python3
"""definining class append_after"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file, after each line containing
    a specific string
    """
    with open(filename, mode='r+', encoding='utf-8') as f:
        contents = f.readlines()
        for index, line in enumerate(contents):
            if search_string in contents[-1]:
                contents.append(new_string)
            if search_string in line:
                contents.insert((index + 1), new_string)
        f.seek(0)
        f.writelines(contents)
