#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    save_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_json_file = __import__('6-load_from_json_file').load_from_json_file

    filename = "add_item.json"
    try:
        my_obj = load_json_file(filename)
    except FileNotFoundError:
        my_obj = []

    save_json_file((my_obj + argv[1:]), filename)
