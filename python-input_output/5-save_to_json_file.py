#!/usr/bin/python3
""" Class Module """


import json


def save_to_json_file(my_obj, filename):
    """ write in json """

    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
