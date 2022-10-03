#!/usr/bin/python3
"""definining class append_after"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file, after each line containing
    a specific string
    """
    with open(filename, mode='r+', encoding='utf-8') as f:
        contents = ""
        for line in f:
            contents += line
            if search_string in line:
                contents += new_string        
        f.seek(0)
        f.writelines(contents)
