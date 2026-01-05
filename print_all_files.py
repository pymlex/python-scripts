"""
This script recursively walks through a given 
directory and prints the contents of all files 
found in that directory and its subdirectories.

The script is intended for exporting the full
textual state of a project tree into a single 
stream.
"""

import os


def print_all_files(root_path: str):
    for dirpath, _, filenames in os.walk(root_path):
        for name in filenames:
            path = os.path.join(dirpath, name)
            print(f"File: {path}")
            with open(path, "r", encoding="utf-8") as f:
                for line in f:
                    print(line.rstrip("\n"))
            print()


if __name__ == "__main__":
    print_all_files("path_to_directory")
