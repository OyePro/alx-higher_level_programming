#!/usr/bin/python3
"""Defining function ``from_json_string``"""
import json


def from_json_string(my_str):
    """
    returns an object by a JSON string
    """
    return (json.loads(my_str))
