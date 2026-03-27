"""
This script is used to remove images from .py files
converted from .ipynb to this format by built-in
Google Colab tools.

The script is needed when the only thing you want is
to process the text or code cells, ignoring base64
encoded images. It also allows you to use much less
file storage.
"""


import sys
import tempfile
import os


def remove_lines_inplace(path: str, prefix: str = "!["):
    dirn = os.path.dirname(path) or "."
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, dir=dirn) as tmp:
        tmp_path = tmp.name
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                if not line.lstrip().startswith(prefix):
                    tmp.write(line)
                else:
                    tmp.write('[illustration]\n')
    os.replace(tmp_path, path)

    print(f"Removed images from {path}")

if __name__ == "__main__":
    remove_lines_inplace("file_name.py")

