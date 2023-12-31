#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys


if __name__ == "__main__":
    load_from_json_file = \
            __import__('6-load_from_json_file').load_from_json_file
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

    filename = "add_item.json"
    argv = []
    try:
        argv = load_from_json_file(filename)
    except FileNotFoundError:
        pass
    argv.extend(sys.argv[1:])
    save_to_json_file(argv, filename)
