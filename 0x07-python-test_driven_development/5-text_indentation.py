#!/usr/bin/python3
"""defining function text_indentation"""


def text_indentation(text):
    """
    return two newlines after ".", "?" and ":"
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for sign in ".?:":
        text = text.replace(sign, sign + "\n\n")
    string_line = "\n".join([line.strip(' ') for line in text.split('\n')])
    print(string_line, end="")
