#!/usr/bin/python3
""" Class Module """


import json


def load_from_json_file(filename):
    """ load form json """

    with open(filename, "r") as f:
        return json.load(f)
