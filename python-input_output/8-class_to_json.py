#!/usr/bin/python3
""" Class Module """


import json


def class_to_json(obj):
    """ class to json function """

    return obj.__dict__
