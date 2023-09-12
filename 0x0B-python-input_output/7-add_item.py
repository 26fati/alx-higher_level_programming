#!/usr/bin/python3
import sys
if __name__ == "__main__":
    load_from_json_file = \
            __import__('6-load_from_json_file').load_from_json_file
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"

# try:
#   argv = load_from_json_file(filename)
# except FileNotFoundError:
argv = sys.argv[1:]

save_to_json_file(argv, filename)
