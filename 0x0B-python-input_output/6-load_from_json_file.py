#!/usr/bin/python3
"""Defining function ``load_from_json_string``"""
import json


def load_from_json_file(filename):
    """
    creates an Object from a “JSON file”
    """
    with open(filename, encoding='utf-8') as fp:
        return (json.load(fp))
