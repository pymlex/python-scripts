"""
This scripts is used to remove metadata from .ipynb files
downloaded from Google Colab. With metadata retained, notebooks 
couldn't be displayed correctly on GitHub, which is a common
issue.

It is a fork of the following project:
https://gist.github.com/drscotthawley/e6927f1389f262ecbabfe41d31989e1c

The issue it intends to fix:
https://github.com/orgs/community/discussions/155944
"""

import json
import sys


def fix_notebook(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    # Remove metadata.widgets entirely (safest approach)
    if 'metadata' in nb and 'widgets' in nb['metadata']:
        del nb['metadata']['widgets']
    
    with open(filename, 'w') as f:
        json.dump(nb, f, indent=2)
    
    print(f"Fixed {filename}")


if __name__ == "__main__":
    fix_notebook('notebook_name.ipynb')
    