#!/usr/bin/python3
"""Defining function ``to_json_string``"""
import json


def to_json_string(my_obj):
    """
    return JSON representation of a string
    """
    return (json.dumps(my_obj))
