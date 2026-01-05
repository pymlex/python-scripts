"""
This script implements the identification of
the encoding of any files. It's definitely
needed when you try to read .csv files with
pandas, as it yields multiple errors on
incorrect character processing due to the
usage of utf-8 by default and the inability to
detect other formats like windows-1251,
etc.

First, install the necessary library:
pip install chardet
"""

import chardet


def get_file_encoding(filename: str) -> str:
    with open(filename, 'rb') as f:
        raw_data = f.read()
        file_description = chardet.detect(raw_data)
        return file_description['encoding']


if __name__ == "__main__":
    encoding = get_file_encoding('file_name')
    print(encoding)